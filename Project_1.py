import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

curr_dir = r"U:\Github_Repo\SeattleAirbnbDataset"
cal_df = pd.read_csv(curr_dir+r"\calendar.csv")
print(cal_df.describe())