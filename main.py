from elasticsearch import Elasticsearch

es = Elasticsearch()

res = es.search(index="catalog")

print('Score: ' + str(res['hits']['max_score']))

for doc in res['hits']['hits']:
    print(doc['_source']['price'])