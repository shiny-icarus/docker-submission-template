FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

RUN apt -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata

RUN apt install -y software-properties-common \
    && apt -y update \
    && add-apt-repository universe

RUN apt-get update && apt install -y python3 python3-pip python3-opencv

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir vtk numba


# Or any preferred Python version.
ADD main.py .
ADD threshold.py .
CMD ["python3", "./main.py"] 
# Or enter the name of your unique directory and parameter set.
