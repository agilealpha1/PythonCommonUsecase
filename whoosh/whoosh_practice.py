from nbformat import write
from sqlalchemy import true
from sympy import content
from whoosh.index import create_in
from whoosh.fields import *
import os
schema =Schema(title=TEXT(stored=true),path=ID(stored=true),content=TEXT)
if not os.path.exists("index"):
    os.mkdir("index")
ix =create_in("index",schema)
writer =ix.writer()

cname = "first dcoument"
pathname ="https://whoosh.readthedocs.io/en/latest/quickstart.html"
content_description= "the descritpion of whoosh "
writer.add_document(title=cname, path=pathname,content=content_description)

writer.add_document(title=u"Second document", path=u"/b",
                 content=u"The second one is even more interesting!")
writer.commit()


from whoosh.qparser import QueryParser
with ix.searcher() as search:
    query = QueryParser("content",ix.schema).parse("second")
    results =search.search(query)
    results[0]
    print (results[0])