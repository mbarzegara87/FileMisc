import requests
from io import BytesIO
from PIL import Image
r=requests.get("https://cdn.vox-cdn.com/thumbor/raooIXhdnitVDcspNDr2nLfJA7M=/0x0:1920x1080/920x613/filters:focal(807x387:1113x693):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/67290668/VRG_TBP_Epic_VS_Apple_Textless.0.jpg")
print(r.status_code)
image=Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path="./image."+image.format
try :
    image.save(path,image.format)
except IOError:
    print("can not save image")

