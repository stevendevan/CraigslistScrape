import pandas as pd


def load_json_to_dataframe(filename):
    try:
        with open(filename) as f:
            dataframe = pd.read_json(f)
    except FileNotFoundError:
        dataframe = pd.DataFrame(columns=['title','id','date','price'])

    return dataframe
