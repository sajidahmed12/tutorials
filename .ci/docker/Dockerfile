FROM 308535385114.dkr.ecr.us-east-1.amazonaws.com/pytorch/pytorch-linux-focal-cuda12.1-cudnn8-py3-gcc9:ba7f4e752ac8ffdec18f81381ed9c25d2962c074

ENV DEBIAN_FRONTEND noninteractive

COPY ./common.sh common.sh
COPY requirements.txt /opt/conda
RUN bash ./common.sh && rm common.sh /opt/conda/requirements.txt

USER jenkins
CMD ["bash"]
