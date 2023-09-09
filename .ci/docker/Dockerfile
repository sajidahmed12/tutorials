FROM 308535385114.dkr.ecr.us-east-1.amazonaws.com/pytorch/pytorch-linux-focal-cuda12.1-cudnn8-py3-gcc9:ba7f4e752ac8ffdec18f81381ed9c25d2962c074

USER root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update || sudo apt-get install libgnutls30
RUN apt-get update
RUN apt-get install -y --no-install-recommends unzip p7zip-full sox libsox-dev libsox-fmt-all rsync

COPY ./common.sh common.sh
COPY ./requirements.txt /opt/conda
RUN bash ./common.sh && rm common.sh /opt/conda/requirements.txt

COPY ./download_data.sh download_data.sh
RUN bash download_data.sh && rm download_data.sh

USER jenkins
CMD ["bash"]
