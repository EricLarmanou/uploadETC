# uploadETC
uploadETC is a python script used by PIs to upload data files to the ICOS carbon portal.

# Usage
- Specify your Station ID
```python
stationID = "GL-ZaF"
```
- update the password to your site
```python
passphrase = "p4ssw0rd"
```
- specify the path of the files to upload
```python
folders = [r"C:\precip",
           r"C:\EC",
           r"C:\met",
           r"C:\SSN",
           r"C:\SSS"]
```
- for each folder specified, specify the file extension
```python
extensions = ['*.dat', '*.zip', '*.dat', '*.dat', '*.dat']
```
