import json 

data = '''
{
  "name":"Banner",
  "phone":"Classified",
  "id" : "Classified",
  "intercom" :{
    "type": "intl",
    "value":"99392933"
  },

  "email" :{
    "hide":"True"
  }
}
'''

info = json.loads(data)
print('Name:',info["name"])
print('ID:',info["id"])
print('Intercom:',info["intercom"]["value"])
print('E-Mail:',info["email"]["hide"])
print("Phone:",info["phone"])

