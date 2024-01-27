from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()

            if exif_data is not None:
                metadata = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value
                return metadata
            else:
                print("No EXIF data found in the image.")
                return None

    except Exception as e:
        print(f"Error opening image: {e}")
        return None
    
def get_date_from_metadata(metadata):
    if 'DateTime' in metadata:
        return metadata['DateTime']
    elif 'DateTimeOriginal' in metadata:
        return metadata['DateTimeOriginal']
    elif 'DateTimeDigitized' in metadata:
        return metadata['DateTimeDigitized']
    else:
        return None
    
image_path = ''
metadata = get_image_metadata(image_path)

if metadata:
    date = get_date_from_metadata(metadata)
    if date:
        print(f"Date taken: {date}")
    else:
        print("Date information not found in metadata.")
else:
    print("Failed to extract metadata from the image.")
