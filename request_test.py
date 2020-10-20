import requests
params={"q":"pizza"}
r = requests.get("http://wwww.bing.com/search",params=params)
print(r.status_code)
print(r.url)
print(r.text)
f = open("./page.html", "w+")
f.write(r.text)
