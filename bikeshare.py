import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from geopy.distance import distance
import pymysql as sql
from geopy.geocoders import Nominatim




# -------------------load data------------------------------------
bike2010 = pd.read_csv("2010-capitalbikeshare-tripdata.csv")
bike2011 = pd.read_csv("2011-capitalbikeshare-tripdata.csv")

bike12Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2012-capitalbikeshare-tripdata/2012Q1-capitalbikeshare-tripdata.csv")
bike12Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2012-capitalbikeshare-tripdata/2012Q2-capitalbikeshare-tripdata.csv")
bike12Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2012-capitalbikeshare-tripdata/2012Q3-capitalbikeshare-tripdata.csv")
bike12Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2012-capitalbikeshare-tripdata/2012Q4-capitalbikeshare-tripdata.csv")

bike13Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2013-capitalbikeshare-tripdata/2013Q1-capitalbikeshare-tripdata.csv")
bike13Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2013-capitalbikeshare-tripdata/2013Q2-capitalbikeshare-tripdata.csv")
bike13Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2013-capitalbikeshare-tripdata/2013Q3-capitalbikeshare-tripdata.csv")
bike13Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2013-capitalbikeshare-tripdata/2013Q4-capitalbikeshare-tripdata.csv")

bike14Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2014-capitalbikeshare-tripdata/2014Q1-capitalbikeshare-tripdata.csv")
bike14Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2014-capitalbikeshare-tripdata/2014Q2-capitalbikeshare-tripdata.csv")
bike14Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2014-capitalbikeshare-tripdata/2014Q3-capitalbikeshare-tripdata.csv")
bike14Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2014-capitalbikeshare-tripdata/2014Q4-capitalbikeshare-tripdata.csv")

bike15Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2015-capitalbikeshare-tripdata/2015Q1-capitalbikeshare-tripdata.csv")
bike15Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2015-capitalbikeshare-tripdata/2015Q2-capitalbikeshare-tripdata.csv")
bike15Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2015-capitalbikeshare-tripdata/2015Q3-capitalbikeshare-tripdata.csv")
bike15Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2015-capitalbikeshare-tripdata/2015Q4-capitalbikeshare-tripdata.csv")

bike16Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2016-capitalbikeshare-tripdata/2016Q1-capitalbikeshare-tripdata.csv")
bike16Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2016-capitalbikeshare-tripdata/2016Q2-capitalbikeshare-tripdata.csv")
bike16Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2016-capitalbikeshare-tripdata/2016Q3-capitalbikeshare-tripdata.csv")
bike16Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2016-capitalbikeshare-tripdata/2016Q4-capitalbikeshare-tripdata.csv")

bike17Q1 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2017-capitalbikeshare-tripdata/2017Q1-capitalbikeshare-tripdata.csv")
bike17Q2 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2017-capitalbikeshare-tripdata/2017Q2-capitalbikeshare-tripdata.csv")
bike17Q3 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2017-capitalbikeshare-tripdata/2017Q3-capitalbikeshare-tripdata.csv")
bike17Q4 = pd.read_csv("/Users/shangshu/PycharmProject/Bikesharing/venv/2017-capitalbikeshare-tripdata/2017Q4-capitalbikeshare-tripdata.csv")


# --------------------------Requirment----------------------------------------
# Project Requirments:
# Use personal git & github for version control, build either Python or R program for analysis.
# Prepare data with data cleansing methods.
# Perform hypothesis testing on the data.
# Apply machine learning models like decision tree, random forest for data classification, feature extraction, etc.
# Generate report with data visualization libraries in R/Python.

# What to submit:
# Screenshots of how you use git commands;
# R/Python codes;
# Final Report. Note: Report should look like the sample report. Make it professional, concise and easy to read.

# # -----------------Where do Capital Bikeshare riders go? TOP 10-----------------------------
# connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select End_station_number, Count(End_station_number) From bike2010 Group BY End_station_number ORDER BY count(End_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2010 Where Start_station_number In (31200,31201,31101,31104,31205,31214,31203,31213,31228,31110)")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)
# Result: TOP 10 2010
# ('14th & V St NW',)
# ('14th & Rhode Island Ave NW',)
# ('Adams Mill & Columbia Rd NW',)
# ('21st & I St NW',)
# ('17th & Corcoran St NW',)
# ('Massachusetts Ave & Dupont Circle NW',)
# ('15th & P St NW',)
# ('20th St & Florida Ave NW',)
# ('17th & K St NW',)
# ('8th & H St NW',)

# connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select End_station_number, Count(End_station_number) From bike2011 Group BY End_station_number ORDER BY count(End_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2011 Where Start_station_number In (31200,31201,31623,31214,31104,31228,31205,31101,31203,31217)")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# Result: TOP10 2011
# ('Adams Mill & Columbia Rd NW',)
# ('14th & Rhode Island Ave NW',)
# ('15th & P St NW',)
# ('14th & V St NW',)
# ('21st & I St NW',)
# ('Columbus Circle / Union Station',)
# ('Massachusetts Ave & Dupont Circle NW',)
# ('17th & Corcoran St NW',)
# ('8th & H St NW',)
# ('USDA / 12th & Independence Ave SW',)
#------------------------ When do they ride? 2010-2017----------------------------------------
# -------whole year --------------
times10 = len(bike2010)
times11 = len(bike2011)
times12 = len(bike12Q1)+len(bike12Q2)+len(bike12Q3)+len(bike12Q4)
times13 = len(bike13Q1)+len(bike13Q2)+len(bike13Q3)+len(bike13Q4)
times14 = len(bike14Q1)+len(bike14Q2)+len(bike14Q3)+len(bike14Q4)
times15 = len(bike15Q1)+len(bike15Q2)+len(bike15Q3)+len(bike15Q4)
times16 = len(bike16Q1)+len(bike16Q2)+len(bike16Q3)+len(bike16Q4)
times17 = len(bike17Q1)+len(bike17Q2)+len(bike17Q3)+len(bike17Q4)
x=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y=[times10, times11, times12, times13, times14, times15, times16, times17]
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('year')
plt.ylabel('numbers of rides')
plt.show()
# ---------season-----------------
S12Q1 = len(bike12Q1)
S12Q2 = len(bike12Q2)
S12Q3 = len(bike12Q3)
S12Q4 = len(bike12Q4)

S13Q1 = len(bike13Q1)
S13Q2 = len(bike13Q2)
S13Q3 = len(bike13Q3)
S13Q4 = len(bike13Q4)

S14Q1 = len(bike14Q1)
S14Q2 = len(bike14Q2)
S14Q3 = len(bike14Q3)
S14Q4 = len(bike14Q4)

S15Q1 = len(bike15Q1)
S15Q2 = len(bike15Q2)
S15Q3 = len(bike15Q3)
S15Q4 = len(bike15Q4)

S16Q1 = len(bike16Q1)
S16Q2 = len(bike16Q2)
S16Q3 = len(bike16Q3)
S16Q4 = len(bike16Q4)

S17Q1 = len(bike17Q1)
S17Q2 = len(bike17Q2)
S17Q3 = len(bike17Q3)
S17Q4 = len(bike17Q4)

x = [1, 2, 3, 4]
y1 = [S12Q1, S12Q2, S12Q3, S12Q4]
y2 = [S13Q1, S13Q2, S13Q3, S13Q4]
y3 = [S14Q1, S14Q2, S14Q3, S14Q4]
y4 = [S15Q1, S15Q2, S15Q3, S15Q4]
y5 = [S16Q1, S16Q2, S16Q3, S16Q4]
y6 = [S17Q1, S17Q2, S17Q3, S17Q4]


x_ticks_labels = ['Spring', 'Summer', 'Autumn', 'Winter']
fig, ax = plt.subplots(1,1)
ax.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6)
# Set number of ticks for x-axis
ax.set_xticks(x)
# Set ticks labels for x-axis
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=18)
plt.ylabel('Number of rides')
plt.legend(('2012','2013','2014','2015','2016','2017'), loc='upper right')
plt.show()

# ----------------------------hour-------------------------------------------
# connecting to the database 2010
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select hour(Start_date), Count(Start_date) From bike2010 Group BY hour(Start_date)Order BY hour(Start_date) ASC;")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# result:
# (0, 1325)
# (1, 891)
# (2, 657)
# (3, 262)
# (4, 123)
# (5, 221)
# (6, 1438)
# (7, 3975)
# (8, 9175)
# (9, 6872)
# (10, 4780)
# (11, 5725)
# (12, 7324)
# (13, 7153)
# (14, 7219)
# (15, 7227)
# (16, 8137)
# (17, 11634)
# (18, 10079)
# (19, 7107)
# (20, 4996)
# (21, 4118)
# (22, 3093)
# (23, 2066)

objects = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
y_pos = np.arange(len(objects))
performance = [1325,891,657,262,123,221,1438,3975,9175,6872,4780,5725,7324,7153,7219,7227,8137,11634,10079,7107,4996,4118,3093,2066]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Number of rides')
plt.ylabel('Hour')
plt.show()

# 2011
# connecting to the database 2011
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select hour(Start_date), Count(Start_date) From bike2011 Group BY hour(Start_date)Order BY hour(Start_date) ASC;")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# Result:
# (0, 15323)
# (1, 9447)
# (2, 6558)
# (3, 3394)
# (4, 1778)
# (5, 5099)
# (6, 20579)
# (7, 56172)
# (8, 94283)
# (9, 58744)
# (10, 46779)
# (11, 55867)
# (12, 68271)
# (13, 68351)
# (14, 65538)
# (15, 67631)
# (16, 84593)
# (17, 126283)
# (18, 115543)
# (19, 84591)
# (20, 61905)
# (21, 48135)
# (22, 37146)
# (23, 24757)


objects = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
y_pos = np.arange(len(objects))
performance = [15323, 9447, 6558, 3394, 1778, 5099,20579,56172,94283,58744,46779,55867,68271,68351,65538,67631,84593,126283,115543,84591,61905,48135,37146,24757]
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Number of rides')
plt.ylabel('Hour')
plt.show()
# -----------------------------------How far do they go?---------------------------------------

# bike2010['distance'] = bike2010.apply(lambda row: distance(row['Start station number'], row['End station number']).miles, axis=1)
# geolocator = Nominatim()
# location = geolocator.geocode("M St & New Jersey Ave SE,31108")
# print(location)
# print((location.latitude,location.longitude))
#
# geolocator = Nominatim(user_agent="Google Map")
# print(geolocator.parse_code(M St & New Jersey Ave SE))


# print((location.latitude,location.longitude))








# # ----------------SQL  Which stations are most popular?----------------------------------
# connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select Start_station_number, Count(Start_station_number) From bike2010 Group BY Start_station_number ORDER BY count(Start_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2010 Where Start_station_number in (31200, 31104, 31201, 31101, 31214, 31203, 31205, 31110, 31602, 31105);")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# result: 2010 TOP 10 start location
# ('Park Rd & Holmead Pl NW',)
# ('14th & Harvard St NW',)
# ('14th & V St NW',)
# ('21st & I St NW',)
# ('15th & P St NW',)
# ('Massachusetts Ave & Dupont Circle NW',)
# ('Adams Mill & Columbia Rd NW',)
# ('14th & Rhode Island Ave NW',)
# ('20th St & Florida Ave NW',)
# ('17th & Corcoran St NW',)


# connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select Start_station_number, Count(Start_station_number) From bike2011 Group BY Start_station_number ORDER BY count(Start_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2010 Where Start_station_number in (31200, 31201, 31623, 31104, 31214, 31101, 31229, 31110, 31203, 31205);")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# Result: 2011 TOP 10 start location
# ('14th & V St NW',)
# ('21st & I St NW',)
# ('15th & P St NW',)
# ('Massachusetts Ave & Dupont Circle NW',)
# ('Adams Mill & Columbia Rd NW',)
# ('14th & Rhode Island Ave NW',)
# ('20th St & Florida Ave NW',)
# ('17th & Corcoran St NW',)
# ('New Hampshire Ave & T St NW',)
# ('Columbus Circle / Union Station',)

# ---------------------------What days of the week are most rides taken on?2010, 2011----------------------------------------

# connecting to the database 2010
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select DAYOFWEEK(Start_date), Count(Start_date) From bike2010 Group BY dayofweek(Start_date)Order BY Count(Start_date) DESC;")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

#  Result:
# (7, 18565)
# (6, 17606)
# (4, 16873)
# (2, 15968)
# (3, 15918)
# (1, 15386)
# (5, 15281)

# connecting to the database 2011
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select DAYOFWEEK(Start_date), Count(Start_date) From bike2011 Group BY dayofweek(Start_date)Order BY dayofweek(Start_date) ASC;")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# Result:
# (1, 174744)
# (2, 177842)
# (3, 178007)
# (4, 167106)
# (5, 172124)
# (6, 179709)
# (7, 177235)

# 2010 vertical bar chart

objects = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
y_pos = np.arange(len(objects))
performance = [15386, 15968, 15918, 16873, 15281, 17606, 18565]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of rides')
plt.show()

# line plot 2010
x = [1, 2, 3, 4, 5, 6, 7]
y1 = [15386, 15968, 15918, 16873, 15281, 17606, 18565]
y2 = [174744, 177842, 178007, 167106, 172124, 179709, 177235]
x_ticks_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fig, ax = plt.subplots(1,1)
ax.plot(x, y1, marker='o')
ax.set_xticks(x)
# Set ticks labels for x-axis
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=11)
plt.ylabel('Number of rides')
plt.show()

# 2011 vertical bar chart
objects = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
y_pos = np.arange(len(objects))
performance = [174744, 177842, 178007, 167106, 172124, 179709, 177235]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of rides')
plt.show()



