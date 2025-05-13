# Etap 1 – instalacja zależności
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Etap 2 – właściwa aplikacja
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
