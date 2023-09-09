FROM python:3.10-alpine as base
LABEL maintainer="eguefif@fastmail.com"
RUN mkdir -p /app
COPY . /app
RUN pip install -e /app/
EXPOSE 10000
ENTRYPOINT ["codingTrackerServer"]
