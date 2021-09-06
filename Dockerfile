FROM python:3.9

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1

WORKDIR /app/user

COPY requirements.txt /app/user/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/user/

ENTRYPOINT ["python"]

CMD ["run.py"]