# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:31:38 2022

@author: Eric Larmanou, Aarhus university, Denmark
upload data files to the ICOS carbon portal, based on instructions from https://github.com/ICOS-Carbon-Portal/data#simplified-etc-specific-facade-api-for-data-uploads
You need to specify station-ID, passphrase, and the folder of the files.
"""

import os
from glob import glob
import hashlib
import requests
import logging

#Settings-----------------------------------------------------------------------------------------------------------
#station ID
#ex: stationID = 'FA-Lso'
stationID = 'FA-Lso'

#passoword
#ex: pwd = 'p4ssw0rd'
pwd = 'p4ssw0rd'

#path mask(s) of the data files
path_masks = [r'C:\precip\*.dat',
           r'C:\EC\*.zip',
           r'C:\met\*.dat',
           r'C:\SSN\*.dat',
           r'C:\SSS\*.dat']
#Initalization------------------------------------------------------------------------------------------------------
#open a log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s> %(message)s',
                    handlers=[logging.FileHandler('uploadETC.log', mode='w'), logging.StreamHandler()],
                    force=True)
#Processing---------------------------------------------------------------------------------------------------------
#loop over path masks
for path_mask in path_masks:
    #log current path mask
    logging.info(' --- Search for files matching: ' + path_mask + ' ---')

    #list the files matching the path mask
    files = sorted(glob(path_mask))

    #loop over files
    NbOk = 0
    for file in files:
        #get the current file name
        basename = os.path.basename(file)

        #log the current filename
        logging.info(basename)

        #open the current file and calculate its checksum
        fid = open(file,'rb')
        checksum = hashlib.md5(fid.read()).hexdigest().upper()
        fid.seek(0)

        #log the current file checksum
        logging.info(checksum)

        #generate the url to upload the current file
        url = 'https://' + stationID + ':' + pwd + '@data.icos-cp.eu/upload/etc/' + checksum + '/' + basename

        #write full url for current file on screen and in log file
        logging.info(url)

        #upload (put) the current file to the server
        result = requests.put(url, data = fid)

        if result.ok:
            NbOk += 1

        #log the result of the request
        logging.info(result.text)

        #close the current file
        fid.close()
        logging.info('-------------------------')

    logging.info('{:d}/{:d} files successfully imported.'.format(NbOk, len(files)))

logging.shutdown()
print(' --- Script ended ---')
