# Aisle 7
A simple script to fetch a Staples employee's work schedule for the day.

## Getting Started
The following instructions will get you up and running with Aisle 7 on your system.

### Prerequisites
The following are required to run Aisle 7
* Mechanize
* BeautifulSoup4

## Running
Aisle 7 requires two parameters
```
-u: Staples employee ID
```
```
-p: Staples Associate Connection password
```

Running the command is as follows
```
./schedule.py -u "<EMPLOYEE_ID>" -p "<PASSWORD>"
```

Example
```
./schedule.py -u "9999999" -p "secur3_p@Ssw0rd!"
2:30PM - 9:00PM
```
