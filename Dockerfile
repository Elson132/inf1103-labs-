FROM python:3.11-slim 
WORKDIR /app
COPY Lesson3/auditor.py .
CMD ["python","auditor.py"]