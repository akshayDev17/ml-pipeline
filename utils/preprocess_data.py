import pandas as pd
import pickle
import json
import pdb
import warnings

# to be erased
from tabulate import tabulate

from pathlib import Path
from utils.feature_tools import FeatureTools
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")


def load_new_training_data(path):
	data = []
	with open(path, "r") as f:
		for line in f:
			data.append(json.loads(line))
	return pd.DataFrame(data)


def build_train(train_path, results_path, dataprocessor_id=0, PATH_2=None):
	target = 'income_label'
	# read initial DataFrame
	df = pd.read_csv(train_path)
	if PATH_2:
		df_tmp = load_new_training_data(PATH_2)
		# Let's make sure columns are in the same order
		df_tmp = df_tmp[df.columns]
		# append new DataFrame
		df = pd.concat([df, df_tmp], ignore_index=True)
		# Save it to disk
		df.to_csv(train_path, index=False)

	# replace >50K with 1 and <= 50K with 0.
	df[target] = (df['income_bracket'].apply(lambda x: '>50K' in x)).astype(int)
	df.drop('income_bracket', axis=1, inplace=True)

	# filter out the 2 types of variables - categorical and continuous
	categorical_columns = list(df.select_dtypes(include=['object']).columns)
	numerical_columns = [c for c in df.columns if c not in categorical_columns+[target]]

	# These are new columns that are the cartesian product of the parent columns.
	crossed_columns = (['education', 'occupation'], ['native_country', 'occupation']) 

	preprocessor = FeatureTools()
	dataprocessor = preprocessor.fit(
		df,
		target,
		numerical_columns,
		categorical_columns,
		crossed_columns,
		sc=MinMaxScaler()
		) # numerical variables are min-max scaled
	# target column is dropped, hence income_label will be dropped,
	# but its values are saved as a separate field

	# binary file
	dataprocessor_fname = 'dataprocessor_{}_.p'.format(dataprocessor_id)
	pickle.dump(dataprocessor, open(results_path/dataprocessor_fname, "wb"))
	if dataprocessor_id==0:
		pickle.dump(df.columns.tolist()[:-1], open(results_path/'column_order.p', "wb"))
		# except the last column, i.e. income_label, save the column list in a binary file

	return dataprocessor


# if __name__ == '__main__':

# 	PATH = Path('data/')
# 	TRAIN_PATH = PATH/'train'
# 	DATAPROCESSORS_PATH = PATH/'dataprocessors'

# 	dataprocessor = build_train(TRAIN_PATH/'train.csv', DATAPROCESSORS_PATH)

