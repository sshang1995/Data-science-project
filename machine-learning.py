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

# count    115597.000000
# mean       1254.649956
# std        2914.317998
# min          60.000000
# 25%         403.000000
# 50%         665.000000
# 75%        1120.000000
# max       85644.000000

member2010 = pd.read_csv("2010member_duration.csv")
plt.hist(member2010['Duration'])
plt.show()
print(member2010['Duration'].describe())

# # count     2000.000000
# # mean      5070.139000
# # std       8239.573878
# # min       2012.000000
# # 25%       2245.000000
# # 50%       2744.500000
# # 75%       4321.500000
# # max      84838.000000

casual2010 = pd.read_csv("2010casual_duration.csv")
plt.hist(casual2010['Duration'])
plt.show()
print(casual2010['Duration'].describe())

# count     2000.000000
# mean     14952.203500
# std      12377.626084
# min       7848.000000
# 25%       9143.500000
# 50%      11023.000000
# 75%      14836.250000
# max      85644.000000

correlations = bike2010.corr()
correlations['Duration']
columns = bike2010.columns.drop(['Duration', 'Start date', 'End date', 'Start station','End station','Bike number','Member type'])


eighty_percent_values = math.floor(bike2010.shape[0]*0.8)
train = bike2010.sample(n=eighty_percent_values, random_state=1)
test = bike2010.drop(train.index)
print(train.shape[0] + test.shape[0] == bike2010.shape[0])

# # linear regression
lr = LinearRegression()
lr.fit(train[columns], train['Duration'])
predictions_test = lr.predict(test[columns])
mse_test = mean_squared_error(test['Duration'], predictions_test)
print(mse_test)
# # 7539610.0724807475
predictions_train = lr.predict(train[columns])
mse_train = mean_squared_error(train['Duration'], predictions_train)
print(mse_train)
# # 8731718.070533177

# Decision tree (single tree model)
tree = DecisionTreeRegressor(min_samples_leaf=5)
tree.fit(train[columns], train['Duration'])
predictions = tree.predict(test[columns])
mse = mean_squared_error(test['Duration'], predictions)
print(mse)
# # 6766705.10485867

# forest of decision trees to reduce overfitting
mse_leaf = []
for i in range(1, 20):
  tree = RandomForestRegressor(min_samples_leaf=i, n_estimators=250)
  tree.fit(train[columns], train['Duration'])
  predictions = tree.predict(test[columns])
  mse= mean_squared_error(test['Duration'], predictions)
  mse_leaf.append(mse)
print(mse_leaf)
# # 6616766.7111575855 min_samples_leaf=13
# [6873602.773215754, 6755740.041481397, 6695071.164118449, 6685513.670888873, 6672799.054870169, 6657093.815563961, 6641673.765914826, 6638367.17182454, 6629401.644702417, 6625532.106051174, 6620994.155261798, 6618572.152731774, 6623565.088072569, 6622036.17940691, 6616959.946677228, 6618096.447912827, 6628064.413332326, 6623737.371340945, 6628235.337853889]

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


# [6621364.930338138, 6618142.8323392, 6618628.508551283] n=500

# ---------------------------------------------------------------------------
# # connecting to the database
connection = sql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='SSnancy0901@', db='Bikeshare')
# cursor
crsr = connection.cursor()
# execute the command
crsr.execute("Select Member_type, count(member_type) From bike2011 Group BY Member_type ORDER BY count(member_type) DESC;")
# store all the fetched data in the ans variable
ans = crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

# Result: 2010
#     ('Member', 91586)
#     ('Casual', 24001)
#     ('Unknown', 10)
# 2011
# ('Member', 979814)
# ('Casual', 246949)
# ('Unknown', 4)



