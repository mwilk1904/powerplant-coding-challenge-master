# Powerplant Coding Challenge

## How to lunch the API

First, you should have Docker installed and have the Docker daemon up and running.

Then execute the following command : 

```bash
docker-compose up -d
```

Now, an API POST endpoint is accessible through [localhost:8888/productionplan](http://localhost:8888/productionplan)

A user-friendly documentation and testing environment are accessible at [localhost:8888/docs](http://localhost:8888/docs)

## How to test the power dispatcher

You should have Python installed as well as the requirements file present in the root of the project.

Then, simply, run the following command : 

```bash
python3 tests.py
```

or


```bash
python tests.py
```

Author : Wilk Marcin 