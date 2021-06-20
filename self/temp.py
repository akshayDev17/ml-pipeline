import pandas as pd
df = pd.read_csv("../data/train/train.csv")
target = 'income_label'
categorical_columns = list(df.select_dtypes(include=['object']).columns)

numerical_columns = [c for c in df.columns if c not in categorical_columns+[target]]
crossed_columns = (['education', 'occupation'], ['native_country', 'occupation'])

print(categorical_columns, "\n", numerical_columns, "\n", crossed_columns)
