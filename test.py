import requests
import json

response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=8Gce4ljbnlx4WWgSACH1rcJBktPVPmRjtMUWBhOt')

print(foodname)
print(type(foodname))
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    # for i in range(len(text)):
    #print(text)
    #print(type(obj))
    
    # for x in obj:
    #     print(obj[x])
    #     print("\n")

    
    #     print(i)
    #print(text)

    for x, y in obj.items():

        #print(type(y))
        #if isinstance(y, dict):

        #if type(y) == int: 


        if type(y) == dict:
            # print(x)
            # print("\n")
            for a,b in y.items():
                # print(a + ":")
                # print(b)
                if a == "pageSize":
                    print(b)
        # print("\n")

jprint(response.json())