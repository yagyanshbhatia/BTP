# BTP
Demonstration portal in flask as part of the bachelor thesis project 


# Steps to run the Portal

## Installing and launching the portal using Flask
1. ```pip3 install flask```
2. ```python3 app.py```

## Installing and running Elastic Search
1. Install Elastic Search and launch it through instructions given here: 
```https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html```
2. Inside main directory (BTP): </br>
```curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@requests_valid.txt"; echo ```
3. To check everything is running properly run: </br>
```curl -XGET 'Localhost: 9200/valid/_count?pretty'``` </br>
This should return this: </br>
```
{
  "count" : 15326,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  }
}
```

## How to use the portal
Go to <code>http://127.0.0.1:5000/</code>
For Demo, go to ```http://127.0.0.1:5000/demo```

## Results
![Screenshot 1](https://github.com/yagyanshbhatia/BTP/blob/master/Screenshots/Screenshot%202020-05-11%20at%207.22.23%20AM.png)

![Screenshot 2](https://github.com/yagyanshbhatia/BTP/blob/master/Screenshots/Screenshot%202020-05-11%20at%207.23.45%20AM.png)

![Screenshot 3](https://github.com/yagyanshbhatia/BTP/blob/master/Screenshots/Screenshot%202020-05-11%20at%207.26.26%20AM.png)

![Screenshot 4](https://github.com/yagyanshbhatia/BTP/blob/master/Screenshots/Screenshot%202020-05-11%20at%207.28.43%20AM.png)

