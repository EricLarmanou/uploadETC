# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:31:38 2022

@author: Eric Larmanou, Aarhus university, Denmark
upload data files to the ICOS carbon portal
converison of the power shell script in python, originl instructions:
The script goes through ALL files within a certain folder and tries to upload them to ICOS-CP
following https://github.com/ICOS-Carbon-Portal/data#simplified-etc-specific-facade-api-for-data-uploads
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
stationID = "GL-ZaF"

# Specify your Passoword here
# eg:   passphrase="p4ssw0rd"
passphrase = "p4ssw0rd"

# specify the path of the files
folders = [r"C:\precip",
           r"C:\EC",
           r"C:\met",
           r"C:\SSN",
           r"C:\SSS"]

#list of extensions for each folder
extensions = ['*.dat', '*.zip', '*.dat', '*.dat', '*.dat']
#-------------------------------------------------------------------------------------------------------------------
#open a log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s> %(message)s',
                    handlers=[logging.FileHandler('uploadETC.log', mode='w'), logging.StreamHandler()],
                    force=True)
#-------------------------------------------------------------------------------------------------------------------
#loop over all folders
for index, folder in enumerate(folders):
    #write current directory on screen
    logging.info(' --- I will search for files here: ' + folder + ' ---')
    
    # Find all files in that folder 
    file_list = glob(os.path.join(folder, extensions[index]))
    
    #loop over all files
    for file in file_list:
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
        
        #write full url for current file on screen
        logging.info(url)
        
        # upload (put) current file to server
        result = requests.put(url, data = fid)
        
        logging.info(result.text)
        
        #close the file
        fid.close()
        logging.info('---------------------------')

logging.shutdown()        
print(' --- Script ended ---')
