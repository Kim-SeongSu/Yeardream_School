import pandas as pd

base_path = 'data/'

def load_dataset(csv_name):
   try:
     df = pd.read_csv(base_path+csv_name)
   except: 
     raise Exception("csv파일명을 입력하세요!")
   return df