#!/usr/bin/env python3
#
# warehouse_data_cleaner.py
#
# VERSION 0.1
#
# AUTHOR: Tina Chen
#
# LAST EDIT: 2019-12-11
#
#This script reads in the amazon warehouse addresses data
#('Amazon-Delivery-Station.csv') and split it into files by
#the year a warehouse was/will be opened (from 2013 to 2020).
#
#User needs to provide the directory of the data file
#and the output files would be stored in the same directory as
#this script

#import modules
import pandas as pd
import os

#get the path of the data file from user
my_dir = input('Enter directory of your data file:')
my_path = os.path.join(my_dir,'Amazon-Delivery-Station.csv')

# Check if the file exists
if not os.path.isfile(my_path):
    print("Invalid file path.")
    quit()

#read data as dataframe
df = pd.read_csv(my_path)

#add the 'country' column and set all values to 'USA'
df['Country']='USA'

#drop unused columns
df = df.drop(['Code','ZIP','Month'],axis=1)

#strip white spaces for values in non-numeric columns
#(numeric columns don't have spaces)
for col in df.columns:
    if col != 'Year':
       df[col]=df[col].str.strip()

#write yearly data into seperate csv files
for i in range(2013,2021):
    f_name = 'delivery_station_%d.csv' % i
    df_y =  df.loc[df['Year']==i]
    df_y.to_csv(f_name, index=False, sep=',')

print('Created output files.')
