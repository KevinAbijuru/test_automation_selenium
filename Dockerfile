# syntax=docker/dockerfile:1

FROM python:3.12-slim AS dependencies

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    SE_AVOID_STATS=true

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /usr/sbin/nologin appuser

WORKDIR /app

COPY --from=dependencies /install /usr/local
COPY app.py ./
COPY includes ./includes

RUN mkdir -p /app/logs \
    && chown -R appuser:appuser /app

USER appuser

CMD ["python", "app.py"]
