import json
def store (variable , filename):
    json.dump(json.dumps(variable), open(filename, "w"))

def retrieve(filename):
    variable = json.loads(json.load(open(filename, "r")))
    return variable