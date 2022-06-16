import data_io
import preprocess_dataset
import learn_model

df_train = data_io.load_dataset("train_V2.csv")
#print(df_train)
#print(df_train.columns)
df_train = preprocess_dataset.preprocess(df_train)
#print(df_train)
#print(df_train.columns)
model = learn_model.learn_ann_model(df_train)


#전체 컬럼 vs 전처리 컬럼
#어떤 컬럼 줄이면 정확도 증가?
#파라미터 어떻게 조절하면 증가?
#발표자료 2~3p로 시각화+약간의 대본 

from lightgbm import plot_importance
import matplotlib.pyplot as plt
%matplotlib inline

fig, ax = plt.subplots(figsize=(10,12))
plot_importance(LGBM_reg, ax = ax)