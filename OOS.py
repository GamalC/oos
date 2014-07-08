import json

from findig import JSONApp
from findig.data import FormParser
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

from api.models.item import Item, get, save, delete

app = JSONApp(
    parser=FormParser()
    )

@app.route("/item/<int:id>")
@app.resource(method_hack=True, name="item")
def item(id):
    item = get(id) or Item({})
    return {"id": item.id, "type": item.type, "title": item.title,
            "content": item.content, "parent": item.parent}

@item.saver
def item(data, id):
    return {"id": save(data, id)}

@item.deleter
def item(id):
    return {"id": delete(id)}

"""
@app.route("/programme")
@app.resource(method_hack=True, name="programme")
def programme():
    return {"id": , "content": }

@app.saver
def programme(data):
    pass

@app.deleter
def programme():
    pass
"""

@app.formatter("application/json")
def format_json(status_code, headers, resource_data, resource):
    return Response(json.dumps(resource_data), status=status_code, 
                    headers=headers, content_type="application/json")


if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True)
