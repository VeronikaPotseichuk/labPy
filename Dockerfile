FROM python:3

WORKDIR /home/veronika/test-docker

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","test.py"]
