from PIL import Image
import imagehash

def compare(img_url1,img_url2):
    hash0 = imagehash.average_hash(Image.open(img_url1)) 
    hash1 = imagehash.average_hash(Image.open(img_url2)) 
    return hash0 - hash1
