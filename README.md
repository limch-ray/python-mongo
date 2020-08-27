# To build this image with docker
```
docker build -t image_name:TAG .
```

# To run this via docker
```
docker run -itd -e MONGO_USER=<mongo user> -e MONGO_PWD=<mongo password> -e MONGO_HOST=<mongo host> -p 5000:5000 image_name:TAG
