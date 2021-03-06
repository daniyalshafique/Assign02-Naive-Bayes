# -*- coding: utf-8 -*-
"""Assignment 03 - Naïve Bayes .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TAOEKpa-DWbRr5NXe_NV8CFhgYuCImb2
"""



# import required library
import pandas as pd
from sklearn.model_selection import train_test_split



# load train data csv file as a dataframe with pandas
train = pd.read_csv("/content/train.csv")
train.head()

# Split train data as t_train and t_test
t_train = train[['Id','Elevation','Aspect','Slope','Horizontal_Distance_To_Hydrology',
                 'Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Hillshade_9am',
                 'Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points','Wilderness_Area1',
                 'Wilderness_Area2','Wilderness_Area3','Wilderness_Area4','Soil_Type1',
                 'Soil_Type2','Soil_Type3','Soil_Type4','Soil_Type5','Soil_Type6','Soil_Type7'
                 ,'Soil_Type8','Soil_Type9','Soil_Type10','Soil_Type11','Soil_Type12','Soil_Type13',
                 'Soil_Type14','Soil_Type15','Soil_Type16','Soil_Type17','Soil_Type18','Soil_Type19',
                 'Soil_Type20','Soil_Type21','Soil_Type22','Soil_Type23','Soil_Type24','Soil_Type25']]
t_test = train[['Soil_Type26','Soil_Type27','Soil_Type28','Soil_Type29','Soil_Type30',
                'Soil_Type31','Soil_Type32','Soil_Type33','Soil_Type34','Soil_Type35','Soil_Type36','Soil_Type37'
                ,'Soil_Type38','Soil_Type39','Soil_Type40','Cover_Type']]

t_train

t_test

from sklearn.model_selection import train_test_split 
t_train , t_test , t_train, t_test = train_test_split(t_train,t_test,test_size=80,random_state= 20)

t_train

t_test

t_train

t_test

# train data in naive bayes
# required library
import numpy as np
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
nvclassifier = GaussianNB()
nvclassifier.fit(t_train, t_test)
y_pred = nvclassifier.predict(t_test)
print(y_pred)

