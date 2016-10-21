FROM continuumio/anaconda3

ENV TF_BINARY_URL https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp35-cp35m-linux_x86_64.whl

RUN pip install --upgrade --ignore-installed $TF_BINARY_URL

WORKDIR "/home"

CMD [ "/bin/bash" ]
