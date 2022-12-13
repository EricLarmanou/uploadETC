# uploadETC
uploadETC is a python script used by PIs to upload data files to the ICOS carbon portal.

# Usage
- Specify your Station ID
```{r, eval = F}
stationID = "GL-ZaF"
```
- update the password to your site
```{r, eval = F}
passphrase = "p4ssw0rd"
```
- specify the path of the files to upload
```{r, eval = F}
folders = [r"C:\precip",
           r"C:\EC",
           r"C:\met",
           r"C:\SSN",
           r"C:\SSS"]
```
-for each folder specified, specify the file extension
```{r, eval = F}
extensions = ['*.dat', '*.zip', '*.dat', '*.dat', '*.dat']
```
