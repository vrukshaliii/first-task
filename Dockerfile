FROM centos:latest

RUN  yum install python3 -y && \
     pip3 install Flask==1.1.1 && \
     pip3 install gunicorn==20.0.4 && \
     pip3 install pandas==0.25.2  && \
     pip3 install scikit-learn==0.23.2  && \
     pip3 install numpy==1.17.3 &&  \
     pip3 install pickle4==0.0.1 && \ 
     pip3 install sklearn==0.0 && \
     mkdir /my_app &&  \
     mkdir -p /my_app/static/css  &&    \
     mkdir /my_app/templates

COPY deploheroku/app.py  /my_app/
COPY deploheroku/FuelConsumption.csv  /my_app/
COPY deploheroku/mlmodel.py  /my_app/
COPY deploheroku/model.pkl /my_app/
COPY deploheroku/static/css/style.css  /my_app/static/css/
COPY deploheroku/templates/index.html /my_app/templates/

EXPOSE  4444

WORKDIR  /my_app

ENTRYPOINT flask  run --host=0.0.0.0    --port=4444
