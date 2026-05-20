FROM python:3.9-slim

WORKDIR /app

COPY backend/ ./backend/
COPY frontend/ ./frontend/

RUN pip install flask

EXPOSE 5000

CMD ["python", "backend/app.py"]