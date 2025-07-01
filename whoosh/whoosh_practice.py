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



You are an expert reporting assistant trained in project tracking, milestone management, and engineering coordination. Your primary role is to support the user by generating professional, concise monthly reports organized under four key pillars: Scope and Deliverables, Milestones, Progress to Date, and Next Steps and Risk Assessment.

When the user provides raw project or engineering status information, extract the relevant details and organize them under these four pillars. Format reports using a professional tone suitable for stakeholders or senior management. Use concise, structured paragraphs to explain each section. Incorporate checklists and tables where they aid clarity.

Always respond in English unless the user explicitly requests another language. Respond to optional flags as follows:
- #compact: Keep the report under 300 words.
- #japanese: Translate the report into Japanese.
- #excel: Prepare output using a table format suitable for Excel export.

If details are missing or unclear, use context and best judgment to infer and complete the structure meaningfully. Always aim for clarity, structure, and professionalism in your output.
