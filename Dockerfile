FROM centos:7
WORKDIR /code
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm -y 
RUN yum -y update
RUN yum -y install python36u python36u-pip git
COPY requirements.txt requirements.txt
RUN pip3.6 install -r requirements.txt
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf", "--log-config", "logging.conf", "-b", ":8080", "main:app"]
