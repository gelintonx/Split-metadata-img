import argparse
from PIL import Image
from PIL.ExifTags import TAGS

# get image path

parser = argparse.ArgumentParser(description='Extract image metadata')
parser.add_argument('-p',help='Get the image path')
args = parser.parse_args()

# open the image
image = Image.open(args.p)

# extracting the exif metadata
exifdata = image.getexif()

print(exifdata)

# looping through all the tags present in exifdata
for tagid in exifdata:

        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)

        # printing the final result
        print(f"{tagname:25}: {value}")
