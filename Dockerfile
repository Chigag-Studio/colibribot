# Set the base image
FROM ubuntu:20.04 AS builder

# Install linux dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y gcc \
        build-essential pkg-config libusb-1.0 curl git \
        sudo && \
    rm -rf /var/lib/apt/lists/*

# Add hummingbot user
RUN useradd -m -s /bin/bash cbot

# Switch to hummingbot user
USER cbot:cbot
WORKDIR /home/cbot/colibribot

# Install miniconda
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh -o ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b && \
    rm ~/miniconda.sh && \
    ~/miniconda3/bin/conda update -n base conda -y && \
    ~/miniconda3/bin/conda clean -tipsy

# Dropping default ~/.bashrc because it will return if not running as interactive shell, thus not invoking PATH settings
RUN :> ~/.bashrc

# Install nvm and CeloCLI; note: nvm adds own section to ~/.bashrc
SHELL [ "/bin/bash", "-lc" ]
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash && \
    export NVM_DIR="/home/cbot/.nvm" && \
    source "/home/cbot/.nvm/nvm.sh" && \
    nvm install 10 && \
    npm install --only=production -g @celo/celocli@1.0.3 && \
    nvm cache clear && \
    npm cache clean --force && \
    rm -rf /home/cbot/.cache

# Copy environment only to optimize build caching, so changes in sources will not cause conda env invalidation
COPY --chown=cbot:cbot setup/environment-linux.yml setup/

# ./install | create hummingbot environment
RUN ~/miniconda3/bin/conda env create -f setup/environment-linux.yml && \
    ~/miniconda3/bin/conda clean -tipsy && \
    # clear pip cache
    rm -rf /home/cbot/.cache

# Copy remaining files
COPY --chown=cbot:cbot bin/ bin/
COPY --chown=cbot:cbot hummingbot/ hummingbot/
COPY --chown=cbot:cbot setup.py .
COPY --chown=cbot:cbot LICENSE .
COPY --chown=cbot:cbot README.md .
COPY --chown=cbot:cbot DATA_COLLECTION.md .

# activate hummingbot env when entering the CT
RUN echo "source /home/cbot/miniconda3/etc/profile.d/conda.sh && conda activate $(head -1 setup/environment-linux.yml | cut -d' ' -f2)" >> ~/.bashrc

# ./compile + cleanup build folder
USER root
RUN /home/cbot/miniconda3/envs/$(head -1 setup/environment-linux.yml | cut -d' ' -f2)/bin/python3 setup.py build_ext --inplace -j 8 && \
    rm -rf build/ && \
    find . -type f -name "*.cpp" -delete

# Build final image using artifacts from builer
FROM ubuntu:20.04 AS release
# Dockerfile author / maintainer 
LABEL maintainer="Chigag Studio / code@chigag.studio >"

# Build arguments
ARG BRANCH=""
ARG COMMIT=""
ARG BUILD_DATE=""
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
LABEL date=${BUILD_DATE}

# Set ENV variables
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}
ENV BUILD_DATE=${DATE}

ENV STRATEGY=${STRATEGY}
ENV CONFIG_FILE_NAME=${CONFIG_FILE_NAME}
ENV WALLET=${WALLET}
ENV CONFIG_PASSWORD=${CONFIG_PASSWORD}

ENV INSTALLATION_TYPE=docker

# Add hummingbot user
RUN useradd -m -s /bin/bash cbot && \
  ln -s /conf /home/cbot/conf && \
  ln -s /logs /home/cbot/logs && \
  ln -s /data /home/cbot/data && \
  ln -s /certs /home/cbot/certs && \
  ln -s /scripts /home/cbot/scripts

# Create mount points
RUN mkdir /conf /logs /data /certs /scripts && chown -R cbot:cbot /conf /logs /data /certs /scripts
VOLUME /conf /logs /data /certs /scripts

# Pre-populate scripts/ volume with default scripts
COPY --chown=cbot:cbot scripts/ scripts/

# Install packages required in runtime
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y sudo libusb-1.0 && \
    rm -rf /var/lib/apt/lists/*

# Switch to hummingbot user
USER cbot:cbot
WORKDIR /home/cbot

# Copy all build artifacts from builder image
COPY --from=builder --chown=cbot:cbot /home/ /home/

# additional configs (sudo)
COPY docker/etc /etc

# Setting bash as default shell because we have .bashrc with customized PATH (setting SHELL affects RUN, CMD and ENTRYPOINT, but not manual commands e.g. `docker run image COMMAND`!)
SHELL [ "/bin/bash", "-lc" ]
CMD /home/cbot/miniconda3/envs/$(head -1 setup/environment-linux.yml | cut -d' ' -f2)/bin/python3 bin/hummingbot_quickstart.py \
    --auto-set-permissions $(id -nu):$(id -ng)
