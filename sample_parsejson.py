import json
import yaml

x = '{"name":"John", "age":"36", "city": "New York City"}'
#parse json

y = json.loads(x)
print("The output of json file is" ,y)
print("Name:",y["name"], "Age:",y ["age"], "City:",y["city"])
