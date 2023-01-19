FROM python:3.9

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir vtk


# Or any preferred Python version.
ADD main.py .
ADD threshold.py .
CMD ["python", "./main.py"] 
# Or enter the name of your unique directory and parameter set.