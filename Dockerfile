FROM python:3.6
ADD . /rakuten_test
WORKDIR /rakuten_test
RUN pip install requests
RUN pip install flask