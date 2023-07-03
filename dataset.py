import torch
# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from torch.utils.data import Dataset


class dataset(Dataset):
    def __init__(self, data, labels):
        self.data = pd.read_csv('data.csv') #loads the csv data into dataframe
        #super(dataset, self).__init__()
        #self.feature = feature
        #self.gt = gt

    def __len__(self):  # 定义自己的数据类，必须重写这个方法（函数）
        return self.gt.size(0)  # 返回的数据的长度

    def __getitem__(self, idx):  # 定义自己的数据类，必须重写这个方法（函数）
        data = (self.feature[idx], self.gt[idx])
        return data

df = pd.read_csv('data.csv')
print(df.head()