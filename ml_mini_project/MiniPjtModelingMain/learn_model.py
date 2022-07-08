from sklearn import metrics
from sklearn.feature_selection import r_regression
from sklearn.model_selection import train_test_split
from lightgbm.sklearn import LGBMRegressor
from sklearn.metrics import mean_absolute_error



def learn_ann_model(df):
  X_train, X_val, y_train, y_val = __divide_training_data(df)
  #LGBM_reg = LGBMRegressor().fit(X_train,y_train)
  LGBM_reg = LGBMRegressor(
    max_depth=10,
    num_leaves=100,
    colsample_bytree=0.7,
    learning_rate=0.3,
    n_estimators=500
  ).fit(X_train,y_train)
  __validate_model(LGBM_reg,X_val,y_val)
  return LGBM_reg


def __divide_training_data(df):
  X = df.drop(['winPlacePerc'],axis=1)
  y = df['winPlacePerc']
  return train_test_split(X, y, test_size = 0.2, random_state=42)


def __validate_model(model,X_val, y_val):
  pred_val = model.predict(X_val)
  print(mean_absolute_error(y_val, pred_val))
    
    

#print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)
#print('--- LGBM Regression ---')
#print('MAE : %.4f' % mean_absolute_error(y_train,pred))
#점수를 높이기 위해 튜닝 or 파라미터 어떤거 조절하면 좋은지 
#activate .fit(X,y)
