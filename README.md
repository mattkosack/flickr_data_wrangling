# Setup

## download.py

You will need to install [exif tool](https://exiftool.org/) to your environment.

You will need to have the exiftool.py [file](https://github.com/smarnach/pyexiftool/blob/master/exiftool.py) in the directory that this script is in.

You will need to directly install the newest version of the Python Flickr Api

    pip3 install git+https://github.com/sybrenstuvel/flickrapi.git

The most updated version is not yet on pypi, and the version on there has issues
with missing xml functions.

Check out the [documentation](https://stuvel.eu/flickrapi-doc/) for more info.

Note: This script uses the Python Flickr API, but the official [Flickr Api](https://www.flickr.com/services/api/) has some more details in the docs. Specifically, the [parameters](https://www.flickr.com/services/api/flickr.photos.search.html) that can be passed into the search are useful. 

You will need to set up a .env file with:

    FLICKR_KEY=[your key]
    FLICKR_SECRET=[your secret]

Which can be received [here](https://www.flickr.com/services/apps/create/apply/).
