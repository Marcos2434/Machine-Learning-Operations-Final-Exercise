# docker build -f train.dockerfile . -t train:latest

# ON ARM
# docker build --platform linux/arm64 -f train.dockerfile . -t train:latest
# docker run --platform linux/arm64 train:latest # OR:
# docker run --name container_name -v "$PWD/models:/models" train:latest # With volume

# If running low on space
# docker system prune

# Base image
FROM python:3.11-slim

# Install Python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY src/ src/
COPY data/ data/

WORKDIR /
RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
# RUN pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

ENTRYPOINT ["python", "-u", "src/main.py", "train"]
