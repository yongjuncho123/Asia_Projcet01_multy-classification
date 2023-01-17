import pandas as pd

# 전치리

# 1. null값 확인해서 채우기

novels = pd.read_csv(r'C:/Users/ChoYJ/Desktop/Data_Study/Asia/1st_team_project(multi_classification)/Asia_Projcet01_multy-classification/Moonpia_clawing_data/Moonpia_clawing_data_50.csv')

novels.tail(10)

novels.isnull().sum()

novels[novels.isna().any(axis=1)] # 데이터 프레임 내 nan값이 있는 행만 출력

### NaN값이 있는 데이터가 적어 파일 내 직접 수정 ###

novels = novels.dropna(axis=0)  

novels[novels.isna().any(axis=1)]

novels.to_csv(r'C:/Users/ChoYJ/Desktop/Data_Study/Asia/1st_team_project(multi_classification)/Asia_Projcet01_multy-classification/Moonpia_clawing_data/Moonpia_clawing_data_pre01.csv', index=False)

### NaN값이 있는 행 2개 삭제

# 2. 제목의 선독점 제거

df_novels = pd.DataFrame()

df_novels.to_csv('./Moonpia_clawing_data/Munpia_crawling_data_final_revise.csv', index = False)

f = open('./Moonpia_clawing_data/Moonpia_clawing_data_pre01.csv', encoding='UTF8')
f2 = open('./Moonpia_clawing_data/Munpia_crawling_data_final_revise.csv', 'w', encoding='UTF8')

line = f.read().replace('선독점', '')

print(line)

f2.write(line)

f.close()
f2.close()

# 3. 제목 & 인트로 합치기


df = pd.read_csv('Moonpia_clawing_data\Munpia_crawling_data_final_revise.csv')

df[df.isna().any(axis=1)] # NaN값 재확인

for i in range(len(df)):
    df['genres'][i] = df['genres'][i].split()[0] # 장르를 하나만 남기기(퓨전 드라마라면 퓨전만 남기기)
for i in range(len(df)):
    df['titles'][i] = df['titles'][i]+df['intros'][i] # 제목과 인트로 합치기

df.drop('intros', axis = 1, inplace = True) # 인트로스를 드랍하고 드랍한 상태를 저장

df.to_csv('./Moonpia_clawing_data/Munpia_pre_final.csv', index=False)