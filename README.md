# BTP
Demonstration portal in flask as part of the bachelor thesis project 


# Steps to run the Portal

## Installing and launching the portal using Flask
1. <code>pip3 install flask</code>
2. <code>python3 app.py</code>

## Installing and running Elastic Search
1. Install Elastic Search and launch it through instructions given here: 
https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html
2. Inside main directory (BTP): </br>
<code>  curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@requests_valid.txt"; echo </code>
3. To check everything is running properly run: </br>
<code>curl -XGET 'Localhost: 9200/valid/_count?pretty'</code> </br>
This should return this: </br>
<code>
{
  "count" : 15326,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  }
}
</code>

## How to use the portal
Go to <code>http://127.0.0.1:5000/</code>

## Results

