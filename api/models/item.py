from database import r

class Item(object):

    def __init__(self, data):
        self.id = data["id"] if data["id"] else -1
        self.content = data["content"] if data["content"] else ""
        self.type = data["type"] if data["type"] else ""
        self.title = data["title"] if data["title"] else ""
        self.parent = data["parent"] if data["parent"] else None

def get(id):
    data = {}
    if r.get("item:%s"):
        if r.get("item:%s:content" % id):
            data['content'] = r.get("item:%s:content" % id)
        if r.get("item:%s:type" % id):
            data['type'] = r.get("item:%s:type" % id)
        if r.get("item:%s:title" % id):
            data['title'] = r.get("item:%s:title" % id)
        if r.get("item:%s:parent" % id):
            data['parent'] = r.get("item:%s:parent" % id)
            
        return Item(data)
    return False

def save(data, id):
    item = Item({})
    if id == -1:
        item.id = r.incr("item_id")
        r.set("item:%s", item.id)
    if data['content']:
        r.add("item:%s:content" % item.id, data['content'])
    if data['type']:
        r.add("item:%s:type" % item.id, data['type'])
    if data['title']:
        r.add("item:%s:title" % item.id, data['title'])
    if data['parent']:
        r.add("item:%s:title" % item.id, data['parent'])
    return item.id

def delete(id):
    if id == -1:
        return False
    r.delete("item:%s:content" % id)
    r.delete("item:%s:type" % id)
    r.delete("item:%s:title" % id)
    r.delete("item:%s:title" % id)
    return id
