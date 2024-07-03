FROM python:3.12-slim-bookworm

ENV SRC_DIR=/lab

ARG USER

RUN useradd -m $USER

ENV PATH="/home/$USER/.local/bin:${PATH}"

WORKDIR $SRC_DIR

RUN chown -R $USER:$USER $SRC_DIR

USER $USER

# Install requirements
COPY ./requirements.txt $SRC_DIR/requirements.txt
RUN pip install --user -r $SRC_DIR/requirements.txt

# Configure Python
ENV PYTHONIOENCODING=utf-8
ENV LC_ALL=C.UTF-8
ENV export LANG=C.UTF-8
ENV PYTHONPATH="${PYTHONPATH}:${SRC_DIR}"
