import pandas as pd
from pathlib import Path
import os
NON_PATH = Path('C:\\Users\\DUC_AN\\Documents\\GitHub\\EEG-ICSSE\\intermediate_datafiles\\motor_imagery\\step3_result\\non_drunk')
DRUNK_PATH = Path('C:\\Users\\DUC_AN\\Documents\\GitHub\\EEG-ICSSE\\intermediate_datafiles\\motor_imagery\\step3_result\\drunk')
all_datasets = []
for instance in os.scandir(NON_PATH): 
    instance_path = instance.path
    dataset = pd.read_csv(instance_path, index_col=0)
    dataset.index = pd.to_datetime(dataset.index)
    all_datasets.append(dataset)
for instance in os.scandir(DRUNK_PATH):
    instance_path = instance.path
    dataset = pd.read_csv(instance_path, index_col=0)
    dataset.index = pd.to_datetime(dataset.index)
    all_datasets.append(dataset)
final = pd.concat(all_datasets, axis=0)
final.to_csv('all_datasets.csv')