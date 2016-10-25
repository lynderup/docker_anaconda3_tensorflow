FROM python:3.5.2

ENV TF_BINARY_URL https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp35-cp35m-linux_x86_64.whl

RUN pip3 install --upgrade --ignore-installed $TF_BINARY_URL
RUN pip3 install --upgrade --ignore-installed ipyparallel

WORKDIR "/root"
RUN mkdir -p .ipython/profile_default/security/
COPY ipcontroller-engine.json .ipython/profile_default/security/
COPY ipcontroller-client.json .ipython/profile_default/security/

WORKDIR "/home"

EXPOSE 2222
EXPOSE 9000-9016

CMD [ "/bin/bash" ]