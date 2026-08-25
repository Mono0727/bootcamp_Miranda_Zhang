import pandas as pd

def fill_missing_median(df, cols):
    df[cols] = df[cols].apply(pd.to_numeric)
    df[cols] = df[cols].fillna(df[cols].median())
    return df

def drop_missing(df, threshold):
    return df.dropna(axis=1, thresh=int(threshold*df.shape[0]))

def normalize_data(df, cols):
    df[cols] = df[cols].apply(pd.to_numeric)
    df[cols] = (df[cols] - df[cols].mean()) / df[cols].std()
    return df