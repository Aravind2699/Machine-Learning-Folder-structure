import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from joblib import dump, load
import datetime
from scripts.data_loader import clean_data, data_feature, data_load_and_preprocess
from scripts.model import build_pipeline

def train():
    pass


