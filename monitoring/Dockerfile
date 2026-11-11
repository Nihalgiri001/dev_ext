FROM python:3.10
WORKDIR /app
RUN pip install flask prometheus_client
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]