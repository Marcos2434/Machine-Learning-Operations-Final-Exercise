# Too lazy to make, smt like this:

# docker run --name evaluate --rm \
#     -v %cd%/models/model.pt:/models/model.pt \  # mount trained model file
#     -v %cd%/data/test_images.pt:/test_images.pt \  # mount data we want to evaluate on
#     -v %cd%/data/test_targets.pt:/test_targets.pt \
#     evaluate:latest \
#     ../../models/trained_model.pt \  # argument to script, path relative to script location in container

# # docker build -f train.dockerfile . -t train:latest

# # ON ARM
# # docker build --platform linux/arm64 -f train.dockerfile . -t train:latest
# # docker run --platform linux/arm64 train:latest # OR:
# # docker run --name container_name -v "$PWD/models:/models" train:latest # With volume

# # If running low on space
# # docker system prune

# # Base image
# FROM python:3.11-slim

# # Install Python
# RUN apt update && \
#     apt install --no-install-recommends -y build-essential gcc && \
#     apt clean && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt requirements.txt
# COPY pyproject.toml pyproject.toml
# COPY src/ src/
# COPY data/ data/

# WORKDIR /
# RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
# # RUN pip install -r requirements.txt --no-cache-dir
# RUN pip install . --no-deps --no-cache-dir

# ENTRYPOINT ["python", "-u", "src/main.py", "evaluate"]
