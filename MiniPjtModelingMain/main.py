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