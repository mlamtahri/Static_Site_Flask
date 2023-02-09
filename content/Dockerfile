FROM continuumio/miniconda3:latest

WORKDIR /Static_Site_Flask/content

COPY conda_flask_env.yaml ./
COPY flask-test.py ./
COPY swagger.json ./
COPY boot.sh ./
COPY templates templates/

RUN chmod +x boot.sh

RUN conda env create -f conda_flask_env.yaml

RUN echo "source activate conda_flask_env" > ~/.bashrc
ENV PATH /opt/conda/envs/conda_flask_env/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]

