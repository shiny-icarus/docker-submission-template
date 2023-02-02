from threshold import threshold
import os

print("This is logged to the server")

# CUDA test code

def cuda_test():
   from numba import cuda
   import numpy as np

   @cuda.jit
   def cudakernel0(array):
      thread_position = cuda.grid(1)
      array[thread_position] += 0.5
   
   array = np.array([0, 1], np.float32)
   print('Initial array:', array)

   print('Kernel launch: cudakernel0[1, 1](array)')
   cudakernel0[1, 2](array)

   print('Updated array:',array)
cuda_test()

# Threshold code

in_path = "/input"
out_path = "/output"
files = os.listdir( in_path )

for file in files:
   ofile = file.split("_")[0] + ".nii.gz" #raw filenames are yyyy_zzzz.nii.gz and segmentation files are yyyy.nii.gz
   ipath = os.path.join(in_path, file)
   opath = os.path.join(out_path, ofile)
   print(ipath, " > ", opath)
   threshold(ipath,opath,1000)
print("end")

