import json 
data = '''[
  {
    "name":"eddy",
    "strength":"kicks",
    "weakness":"anything"
  },

  {
    "name":"Paul",
    "strength":"MAXIMA",
    "weakness":"legs"
  },
  {
    "name":"nina",
    "strength":"venom",
    "weakness":"toe-to-toe"
  },
  {
    "name":"YOSHIMITSU",
    "strength":"SLIDER KICKS",
    "weakness":"Long range fight"
  }
]'''

info = json.loads(data)
for item in info:
  print('Name:',item['name'])
  print('Strength:',item['strength'])
  print('Weakness:',item['weakness'])
  print("\n")

