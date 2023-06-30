import pandas as pd 

# series
sr = pd.Series(["삼성전자", "LG에너지솔루션", "SK하이닉스", "삼성바이오로직스"],
index=["005930", "373220", "000660", "207940"])

# csv입출력
print(sr)
print(sr.values)
print(sr.index)

# DataFrame
hong = ["20011300", "홍길동", "경영학과", 70, 80, 100, 50]
kim = ["20021288", "김길동", "무역학과", 85, 90, 80, 80]
lee = ["20021009", "이길동", "경제학과", 100, 60, 65, 75]
park = ["20011176", "박길동", "경제학과", 100, 75, 30, 55]
ko = ["20011894", "고길동", "경영학과", 90, 80, 100, 100]

data = [hong, kim, lee, park, ko]
df = pd.DataFrame(data)

header =["학번", "이름", "학과", "출석", "과제", "중간", "기말"]
df = pd.DataFrame(data, columns=header)
print(df)

df.head(3) # 0번 행부터 3개 조회
df.tail(3) # 마지막 행(row)부터 3개 행 조회
df["학번"] # "학번" 열(column) 조회
df[["학번", "학과"]] # "학번", "학과" 열(column) 조회
# 인덱스(index)로 조회
df.loc[1] # 1번 인덱스 행 레코드 조회
df.loc[1, "이름"] # 1번 인덱스 행 레코드 중 "이름" 열 값 조회
df.loc[1]["이름"]
df.loc[1, ["이름", "학과"]] # 1번 인덱스 행 레코드 중 "이름", "학과" 열 값 조회
df.loc[df["학과"]=="경영학과", "이름"] # 조건을 충족하는 레코드 조회
# 행(row) 번호로 조회
df.iloc[1] # 1번 행 레코드 조회
df.iloc[1, 1] # 1번 행 레코드 중 1번 열 값 조회
df.iloc[1][1]
df.iloc[1, [1, 2]] # 1번 행 레코드 중 1, 2번 열 값 조회
# groupby
groups = df.groupby("학과")
for g, d in groups:
    print("학과:", g)
    print(d)