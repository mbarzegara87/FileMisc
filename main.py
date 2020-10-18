import simplejson as json
import os


if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size is not 0:
    old_file=open("./ages.json","r+")
    data=json.loads(old_file.read())
    print(data["age"])
    data["age"]=data["age"]+1
else:
    old_file=open("./ages.json","w+")
    data={"Name":"Nick","age":24}
    print("No file found ")

old_file.seek(0)
old_file.write(json.dumps(data))



