# vlog
### simple website visitor logging

This is a no-frills website traffic monitoring tool.  
It simply appends _visitor IP_, _datetime_, and _user-agent_ information
to a file called "vlog.txt".

On the server-side PHP (vlog.php) is used to append this info to vlog.txt:  
>
`14.29.200.97,2023-08-15 14:23:42,Mozilla/5.0 (iPhone; CPU iPho ...`

---

Collection and reporting begins with a `wget` to retrieve the vlog.txt file for a particular site.

| FILES | DESCRIPTIONS |
| --- | --- |
|vlog.txt            | log file created on the website root|
|ip2loc_vlog.py      | process vlog to report|
|ip2loc_vlog_csv.py  | process vlog to csv file|
|vlog_report.sh      | run report for one site|
|vlog_sheet.sh       | run spreadsheet for one site
|runall_reports.sh   | run reports for all sites|
|runall_sheets.sh    | run spreadsheets for all sites|
|ip2locationIPV4.db  | ip2location database|

---

```text
 SAMPLE REPORT:

 - - - - - - - - - - - - - - - - - - - - - - -
           IP:  216.218.206.68
         Time:  2023-08-15 02:40:50
 country code:  US
 country name:  United States of America
  region name:  California
    city name:  Fremont
   User Agent:  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...
 https://maps.google.com/?q=37.517979,-121.929488
 - - - - - - - - - - - - - - - - - - - - - - -
           IP:  45.156.129.32
         Time:  2023-08-14 23:47:51
 country code:  BE
 country name:  Belgium
 
 SAMPLE CSV FILE:
 
 IP,DATE_TIME,CODE,NAME,REGION,CITY,LAT,LON,USER_AGENT
 216.218.206.68,2023-08-15 02:40:50,US,United States of America,California,Fremont,37.517979,-121.929488 Mozilla/5.0...
 45.156.129.32,2023-08-14 23:47:51,BE,Belgium Brussels,Hoofdstedelijk Gewest,Brussels,50.85045,4.34878,Mozilla/5.0 ...
 
```
---

NOTE: the file ip2locationIPV4.db which is too large to upload here was
constructed from a download from this website:

> https://lite.ip2location.com/database/ip-country

```sql

CREATE TABLE "ip" (
	`ip_from` INTEGER,
	`ip_to` INTEGER,
	`country_code` TEXT,
	`country_name` TEXT,
	`region_name` TEXT,
	`city_name` TEXT,
	`latitude` TEXT,
	`longitude` TEXT
)

```
