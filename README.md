# Application Documentation

## Install tools

### git
```
sudo apt install git
```

### docker engine
```
https://docs.docker.com/engine/
```

### docker-compose
```
sudo apt install python-pip
sudo pip install docker-compose
```

## Usage
### Build and run
```
sudo docker-compose build
sudo docker-compose up -d
```

### Usage
1. Generate Records with r_value between 1000 and 9999
```
http://localhost:5000/generate/
```
2. Show Records with r_value over 9000
```
http://localhost:5000/show_records/
```







