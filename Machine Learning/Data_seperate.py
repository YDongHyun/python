import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

titanic = pd.read_csv('./data/titanic.csv')
titanic_1 = titanic.drop(columns=['Cabin'])

# 결측값 존재하는 샘플 제거
titanic_2 = titanic_1.dropna()

# 이상치 처리
titanic_3 = titanic_2[titanic_2['Age']-np.floor(titanic_2['Age']) == 0 ]
print('전체 샘플 데이터 개수: %d' %(len(titanic_3)))

"""
1. feature 데이터와 label 데이터를 분리
"""
X = titanic_3.drop(columns=['Survived']) #survived 삭제
y = titanic_3['Survived'] #survived만 분리
print('X 데이터 개수: %d' %(len(X)))
print('y 데이터 개수: %d' %(len(y)))

"""
2. 학습용, 평가용 데이터로 분리
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#테스트 30%를 테스트로, 나머지는 학습용으로 사용
#랜덤시드값은 랜덤으로 뽑는다.

# 분리한 데이터의 개수를 출력
print('학습용 데이터 개수: %d' %(len(X_train)))
print('평가용 데이터 개수: %d' %(len(X_test)))
