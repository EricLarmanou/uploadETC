# uploadETC
uploadETC is a python script used by PIs to upload data files to the ICOS carbon portal.

# Usage
- Specify your Station ID
```python
stationID = "FA-Lso"
```
- update the password to your site
```python
pwd = "p4ssw0rd"
```
- specify the mask(s) of the data files to upload
```python
folders = [r"C:\precip\*.dat",
           r"C:\EC\*.zip",
           r"C:\met\*.dat",
           r"C:\SSN\*.dat",
           r"C:\SSS\*.dat"]
```
