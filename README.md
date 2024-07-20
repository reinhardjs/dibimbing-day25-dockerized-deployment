### How to run in local

```
uvicorn main:app -—host 0.0.0.0 -—port 8888
```

### How to build docker image

```
docker build -t dibimbing-ml-docker:v1.0 .
```

### How to run as docker container

```
docker run --name dibimbing-ml-docker -p 1234:8001 dibimbing-ml-docker:v1.0
```
