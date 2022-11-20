  FROM python:3.8-alpine
  LABEL maintainer="Kunal Malhotra, kunal.malhotra1@ibm.com"
  RUN mkdir /app
  WORKDIR /app
  COPY . /app
  RUN pip install flask
  EXPOSE 5000
  ENTRYPOINT [ "python" ]
  CMD [ "app.py" ]