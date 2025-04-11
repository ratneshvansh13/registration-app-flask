FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py", "run", "--host=0.0.0.0" ]
# Expose the port the app runs on
EXPOSE 5000
# Expose the port the app runs on
# EXPOSE 5000
