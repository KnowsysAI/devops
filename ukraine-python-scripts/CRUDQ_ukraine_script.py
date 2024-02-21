import requests
url = "https://search-newsdata-tester-uy43guqnasvykkyt5wkmx4y7sa.us-east-1.es.amazonaws.com/ukraine_index"
username = "ethanfincher"
password = "Password123!"

#read
#just needs the _search part to get everything
#otherwise it gets the details of the index rather then whats inside it
def get_all_data():
    get_response = requests.get(f"{url}/_search", auth=(username, password))
    print (get_response.text)

#create/update
#my understanding is that you can update and create with either PUT or POST
#but the docs recommend you PUT when you want to create (unless your doing automatic ID generation or bulk inserts)
#and do a POST for updates and bulk actions
#you can read a json file and do a bulk insert with it, but it needs to be in a specific format (link for demo below)
#you can also add random stuff to the mapping of the index, which is really dumb, so we should keep out objects very well defined
#or find some way to deny requests for updates and creations that dont match the mapping
def create_data():
    create_string = '{"title": "British father makes it to wife and son after two-day journey to Ukraine", "link": "https://ca.sports.yahoo.com/news/british-father-makes-wife-son-135048059.html?src=rss", "keywords": null, "creator": null, "video_url": null, "description": null, "content": null, "pubDate": "2022-03-01 13:50:48", "expire_at": "Wed, 07 Sep 2022 13:50:48 GMT", "image_url": null, "source_id": "yahoo", "country": ["canada"], "category": ["sports"], "language": "english"}'
    create_response = requests.put(f"{url}/_doc/10", 
                                    data= create_string,
                                    headers={'Content-Type': 'application/json'},
                                    auth=(username, password))
    print (create_response.text)

def edit_data():
    edit_string = '{"title": "British father makes it to wife and son after two-day journey to Ukraine", "link": "https://ca.sports.yahoo.com/news/british-father-makes-wife-son-135048059.html?src=rss", "keywords": null, "creator": null, "video_url": null, "description": null, "content": null, "pubDate": "2022-03-01 13:50:48", "expire_at": "Wed, 07 Sep 2022 13:50:48 GMT", "image_url": "www.pictureoffrogs.com", "source_id": "yahoo", "country": ["canada"], "category": ["sports"], "language": "english"}'
    update_response = requests.post(f"{url}/_doc/10", 
                                    data= edit_string,
                                    headers={'Content-Type': 'application/json'},
                                    auth=(username, password))
    print (update_response.text)

#delete
#nice and simple, just throw the item type (_doc) annd the id and it deletes it.
#doing bulk deletes is simple, theres a quick guide down on the bottom
def delete_data():
    delete_response = requests.delete(f"{url}/_doc/10", auth=(username, password))
    print (delete_response.text)

#query
#searching can get pretty complicated, I'll add the link to the AWS guide for it
#theres the simple one where you just add one or 2 things into the URI
#the one we would probably build and use is the one that uses the request body
#you can do a ton of detailed searching with it. Ill add simple examples of both down below
#https://docs.aws.amazon.com/opensearch-service/latest/developerguide/searching.html
def simple_query():
    simple_query_response = requests.get(f"{url}/_search?q=title:UK", auth=(username, password))
    print (simple_query_response.text)
def complex_query():  
    search_string = '''{
                        "query": {
                            "match": {
                            "title": "british"
                            }
                        }
                        }'''
    complex_query_response = requests.get(f"{url}/_search",
                            data=search_string,
                            headers={'Content-Type': 'application/json'},
                            auth=(username, password))
    print (complex_query_response.text)
#bulk
#last little detail for the basics, if you want to do a bulk anything, you do make a POST request
#each type of action has its own format, link to good instructions below, but ill do a simple syntax example
# def bulk_operation():
#     bulk_string = '''{ "delete": { "_index": "movies", "_id": "tt2229499" } }
# { "index": { "_index": "movies", "_id": "tt1979320" } }
# { "title": "Rush", "year": 2013 }
# { "create": { "_index": "movies", "_id": "tt1392214" } }
# { "title": "Prisoners", "year": 2013 }
# { "update": { "_index": "movies", "_id": "tt0816711" } }
# { "doc" : { "title": "World War Z" } }'''
#     bulk_response = requests.post(f"{url}/_bulk",
#                             data=bulk_string,
#                             auth=(username, password))

#tiny little script to run what i want
command = ""
while(command != "n"):
    while(command not in ("c", "r", "u", "d", "q", "f")):
        command = input('please enter one of the following: \ncreate (c)\nread all (r)\nupdate (u)\ndelete (d)\nsimple query (q)\nfancy query (f)\n').lower()
    if command == "c":
        create_data()
    elif command == "r":
        get_all_data()
    elif command == "u":
        edit_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        simple_query()
    elif command == "f":
        complex_query()
    command=""

#helpful links that ive used so far
#basics of adding and searching docs in an index, "getting started" stuff
#https://docs.aws.amazon.com/opensearch-service/latest/developerguide/quick-start.html
#https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html
#indexing a doc in more detail
#https://opensearch.org/docs/1.2/opensearch/rest-api/document-apis/index-document/
#querying in detail
#https://docs.aws.amazon.com/opensearch-service/latest/developerguide/searching.html
#updating a doc in detail
#https://opensearch.org/docs/latest/api-reference/document-apis/update-document/
#bulk actions
#https://opensearch.org/docs/latest/api-reference/document-apis/bulk/