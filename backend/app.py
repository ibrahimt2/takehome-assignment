


from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")

@app.route("/shows/<id>", methods=['GET'])
def get_specific_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.getById('shows', int(id))
    return create_response(db.getById('shows', int(id)))

@app.route("/shows", methods=['POST'])

def create_new_show():

    data = request.get_json()
 
    #Checks to see if the JSON body has a dictionary entry with key 'name', returns error if not
    if 'name' in data:
        name = data['name']
    else:
        return create_response(message="You must enter a name", status = 422)

    #Checks to see if the JSON body has a dictionary entry with key 'episodes_seen', returns error if not
    if 'episodes_seen' in data:
        episodes_seen = data['episodes_seen']
    else:
        return create_response(message="You must enter the number of episodes seen", status = 422)

    #Creates new entry
    new_entry = db.create("shows", {"name" : name, "episodes_seen" : episodes_seen})

    return create_response(new_entry, status = 202, message="Your show has successfully been added")
    
@app.route("/shows/<id>", methods=['PUT'])

def update_show(id):

    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")

    data = request.get_json()
    updatedEntry = db.updateById("shows", int(id), data)
    return create_response(updatedEntry, message="Your show has been updated")


# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
