# Overview
This report is about capital bikeshare data analysis. The dataset comes from capital Bikeshare website. The data from 2010 to 2017, each csv file has 7 columns. Capital Bikeshare is metro DC's bikeshare service, with 4,300 bikes and 500+ stations across 6 jurisdictions: Washington, DC.; Arlington, VA; Alexandria, VA; Montgomery, MD; Prince George's County, MD; and Fairfax County, VA. Designed for quick trips with convenience in mind, it's a fun and affordable way to get around. I used python and SQL to do data analysis and explained several questions about users' behavior. And I applied machine learning methods (decision tree and random forest) to predict duration of bike using.
# Research questions
## 1. where so capital bikeshare riders go?
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pymysql as sql

# connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='*****', db='Bikeshare')
crsr = connection.cursor()
# execute the command
crsr.execute("Select End_station_number, Count(End_station_number) From bike2010 Group BY End_station_number ORDER BY count(End_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2010 Where Start_station_number In (31200,31201,31101,31104,31205,31214,31203,31213,31228,31110)")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)
    
#2011 
crsr.execute("Select End_station_number, Count(End_station_number) From bike2011 Group BY End_station_number ORDER BY count(End_station_number) DESC LIMIT 10;")
crsr.execute("Select DISTINCT Start_station From bike2011 Where Start_station_number In (31200,31201,31623,31214,31104,31228,31205,31101,31203,31217)")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)
    
```
### Year 2010 TOP 10 locations riders go
1.	14th & V St NW
2.	14th & Rhode Island Ave NW
3.	Adams Mill & Columbia Rd NW
4.	21st & I St NW
5.	17th & Corcoran St NW
6.	Massachusetts Ave & Dupont Circle NW
7.	15th & P St NW
8.	20th St & Florida Ave NW
9.	17th & K St NW
10.	8th & H St NW
### Year 2011 TOP 10 Locations riders go
1.	Adams Mill & Columbia Rd NW
2.	14th & Rhode Island Ave NW 
3.	15th & P St NW
4.	14th & V St NW
5.	21st & I St NW
6.	Columbus Circle / Union Station
7.	Massachusetts Ave & Dupont Circle NW
8.	17th & Corcoran St NW
9.	8th & H St NW
10.	USDA / 12th & Independence Ave SW

## 2. When do they ride?
![image](https://github.com/sshang1995/Data-science-project/blob/master/Year_number.png)
From 2010 to 2017, the number of rides increasing dramatically, it is clear that riding a bike is a new fashion for city people. More and more people choose to take a bike to go to different places.

![image](https://github.com/sshang1995/Data-science-project/blob/master/season.png)

Through the figure above, people prefer to ride bikes in Summer and Autumn than in Spring and Winter. The mainly reason is environmental temperature in summer and autumns are more suitable for people to go outside.
Comparing data from 2012 to 2017, Autumn is the most popular season for people riding bike. Why? In my opinion, people rode all summer long, Autumn is the cool weather making getting on your bike that much more enjoyable.

![image](https://github.com/sshang1995/Data-science-project/blob/master/2010.png) 2010 data
![image](https://github.com/sshang1995/Data-science-project/blob/master/2011.png) 2011 data

The most popular time of riding is 8-9 am and 5-6 pm. More and more people choose to ride a bike to go to work/school. Comparing data from 2010 and 2011, it is clear that the data trend looks similar, that means riders have fixed habit to ride bikes and the capital bikeshare company has a large number of fixed users which guarantee the business operation stably over years.

### What days of the week are the most rides taken on?
![image](https://github.com/sshang1995/Data-science-project/blob/master/2010weekday.png) 2010 data
![image](https://github.com/sshang1995/Data-science-project/blob/master/2011weekday.png) 2011 data

# Machine learning 
## Predicting bike using duration with decision trees
we are going to look at dataset that contains duration of rental bikes. From the dataset, we are going to apply various machine learning algorithms to generate a model that can predict the duration of bike using.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pymysql as sql
import math

 # -------------------load data------------------------------------
bike2010 = pd.read_csv("2010-capitalbikeshare-tripdata.csv")
plt.hist(bike2010['Duration'])
plt.show()
print(bike2010['Duration'].describe())

# define train data and test data
correlations = bike2010.corr()
correlations['Duration']
columns = bike2010.columns.drop(['Duration', 'Start date', 'End date', 'Start station','End station','Bike number','Member type'])

eighty_percent_values = math.floor(bike2010.shape[0]*0.8)
train = bike2010.sample(n=eighty_percent_values, random_state=1)
test = bike2010.drop(train.index)
print(train.shape[0] + test.shape[0] == bike2010.shape[0])
```

```python
#  linear regression
lr = LinearRegression()
lr.fit(train[columns], train['Duration'])
predictions_test = lr.predict(test[columns])
mse_test = mean_squared_error(test['Duration'], predictions_test)
print(mse_test)
```
MSE = 7539610.07
Using linear regression to predict train data, the result shows high MSE. Most of predict value focus on 1260-1270, while the mean value of duration is 1254. So, the predict value is close to mean value of the duration.

```python
# Decision tree (single tree model)
tree = DecisionTreeRegressor(min_samples_leaf=5)
tree.fit(train[columns], train['Duration'])
predictions = tree.predict(test[columns])
mse = mean_squared_error(test['Duration'], predictions)
print(mse)
```
MSE = 6766705.10
As we can see, the decision tree model reduced our error significantly. We can further improve our result using a forest of decision trees to reduce overfitting.

```python
# forest of decision trees to reduce overfitting
mse_leaf = []
for i in range(1, 20):
  tree = RandomForestRegressor(min_samples_leaf=i, n_estimators=250)
  tree.fit(train[columns], train['Duration'])
  predictions = tree.predict(test[columns])
  mse= mean_squared_error(test['Duration'], predictions)
  mse_leaf.append(mse)
print(mse_leaf)

n_trees =[250, 500, 750]
mse_trees =[]
for i in n_trees:
    tree = RandomForestRegressor(min_samples_leaf=13, n_estimators=i)
    tree.fit(train[columns], train['Duration'])
    predictions = tree.predict(test[columns])
    mse = mean_squared_error(test['Duration'], predictions)
    mse_trees.append(mse)
print(mse_trees)

tree = RandomForestRegressor(min_samples_leaf=13, n_estimators=500)
tree.fit(train[columns], train['Duration'])
predictions = tree.predict(test[columns])
mse = mean_squared_error(test['Duration'], predictions)
```
MSE = 6618142.83
I specified the hyperparameter values 'min_samples_leaf' and 'n_estimators', I optimized these values by using a for loop. Using 500 trees and 13 min_samples_leaf, MSE lower to 6618142
