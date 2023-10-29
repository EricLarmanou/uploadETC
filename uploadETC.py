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

#-------------------------------------------------------------------------------------------------------------------
# VARIABLES to specify

# Specify your Station ID
# eg:  station="FA-Lso"
stationID = "FA-Lso"

# Specify your Passoword here
# eg:   passphrase="p4ssw0rd"
passphrase = "p4ssw0rd"

# specify the mask of the data files
folders = [r"C:\precip\*.dat'",
           r"C:\EC\*.zip'",
           r"C:\met\*.dat'",
           r"C:\SSN\*.dat'",
           r"C:\SSS\*.dat'"]
#-------------------------------------------------------------------------------------------------------------------
#open a log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s> %(message)s',
                    handlers=[logging.FileHandler('uploadETC.log', mode='w'), logging.StreamHandler()],
                    force=True)
#-------------------------------------------------------------------------------------------------------------------
#loop over all folders
for index, path_mask in enumerate(path_masks):
    #write current directory on screen
    logging.info(' --- Search for files matching: ' + path_mask + ' ---')
    
    # Find all files in that folder 
    files = sorted(glob(path_mask))
    
    #loop over all files
    NbOk = 0
    for file in files:
        basename = os.path.basename(file)
        #write current filename on the screen
        logging.info(basename)                                                      
        
        #calculate the checksum of the current file
        fid = open(file,'rb')
        checksum = hashlib.md5(fid.read()).hexdigest().upper()
        fid.seek(0)
        
        #write checksum of current file on the screen
        logging.info(checksum)
        
        #generate full url for current file
        url = 'https://' + stationID + ':' + passphrase + '@data.icos-cp.eu/upload/etc/' + checksum + '/' + basename
        
        #write full url for current file on screen and in log file
        logging.info(url)
        
        # upload (put) current file to server
        result = requests.put(url, data = fid)
        
        if result.ok:
            NbOk += 1
        
        logging.info(result.text)
        
        #close the file
        fid.close()
        logging.info('---------------------------')
    
    logging.info('{:d}/{:d} files successfully imported.'.format(NbOk, len(files)))

logging.shutdown()
print(' --- Script ended ---')
