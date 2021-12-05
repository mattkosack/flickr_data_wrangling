import os
import time
import dotenv
import urllib
import flickrapi
import exiftool
import json
import xml.etree.ElementTree as ET

"""
NOTE: Since we just keyboard interrupt the program, 
    you will have to add the closing bracket ']' to the end of the file 
    and delete the last comma.
"""

def get_xml(filename, photos, num_images):
    """
    A testing function to get the xml response from flickr.
    """
    with open(filename, 'w') as f:
        for i, photo in enumerate(photos):
            if i > num_images:
                break
            f.write(str(ET.tostring(photo)) + '\n')

def get_exif_data(filename, photos, tag):
    """
    Download the original image from flickr and write its exif data to a json.
    """
    with open(filename, 'a') as exif_file:
        with exiftool.ExifTool() as et:
            for i, photo in enumerate(photos):

                # Photo info from flickr
                url = photo.get('url_o')
                im_ID = photo.get('id')
                lat = photo.get('latitude')
                lon = photo.get('longitude')
                accuracy = photo.get('accuracy')
                date_taken = photo.get('datetaken')

                name = f'images/img_{tag}_{i}.jpg'

                try:
                    # save the image
                    urllib.request.urlretrieve(url, name)

                    # get the exif data
                    metadata = et.get_metadata(name)

                    # add our requested data
                    metadata['Image_ID'] = im_ID
                    metadata['Latitude'] = float(lat)
                    metadata['Longitude'] = float(lon)
                    metadata['Accuracy'] = int(accuracy)
                    metadata['Date_Taken'] = date_taken

                    # Write the data
                    # exif_file.write(json.dumps(metadata, separators=(',', ':')) + ',\n') # This will print in a readable way
                    exif_file.write(json.dumps(metadata, indent=4) + ',\n') # This prints one json per line

                    # Delete the image after getting its info
                    os.remove(name)

                except Exception as e:
                    # TODO: Need way better error catching
                    with open('log.txt', 'a') as log:
                        log.write(str(e) + '\n')
                    pass

                # Wait to download the next
                # TODO: Need more efficient use of api calls
                time.sleep(2)



def main():
    dotenv.load_dotenv()

    KEY = os.getenv('FLICKR_KEY')
    SECRET = os.getenv('FLICKR_SECRET')
    flickr = flickrapi.FlickrAPI(KEY, SECRET)
    output_file = 'exif_data/exif_data.json'

    tag = 'landscape'

    photos = flickr.walk(text=tag, 
                        tag_mode='all', 
                        tags=tag, 
                        extras='url_o, geo, date_upload, date_taken', # needs to be a long string 'list'
                        per_page=100, 
                        sort='relevance')

    # for viewing returned info
    # get_xml('test.txt', photos, 1)

    # Write the exif data and append api return info
    get_exif_data(output_file, photos, tag)


if __name__=='__main__':
    main()

