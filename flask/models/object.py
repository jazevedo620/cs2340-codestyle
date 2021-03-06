from flask_restful import Resource
from flask_restful import reqparse

# Intentionally formatted poorly to check pylint functionality
objects = {"ball": "red", "clown": "fun"}
def formatMessage(name, message):
    return ("Object {} {}".format(name, message))
class Object( Resource ):
    def get(self, newNAME ):
        if newNAME in objects.keys():    return objects[ newNAME ],   200
        else: return formatMessage(newNAME, "not found"), 404
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('value')
        args = parser.parse_args()
        if args.get('value') is None:
            return "Malformed request", 400
        else:
            if name not in objects.keys():
                objects[name]=args.get( 'value')
                return formatMessage(name, "created successfully").format(name),201
            else:
                return "Object {} already exists".format(name),402
    def delete(self, name):
        if (name in objects.keys()):
            del objects[name]
            return "Object {} deleted".format(
                name),   200
        else:
            return formatMessage(name, "not found"), 404
