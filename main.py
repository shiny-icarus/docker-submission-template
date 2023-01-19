from threshold import threshold
import os

print("This is logged to the server")

in_path = "/input"
out_path = "/output"
files = os.listdir( in_path )

for file in files:
   ipath = os.path.join(in_path, file)
   opath = os.path.join(out_path, file)
   print(ipath, " > ", opath)
   threshold(ipath,opath,1000)
print("end")

