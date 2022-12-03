#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def uniqueVal(df,col):
    #display unique values count of a dataframe column
    print(df[col].value_counts(dropna=False))

# Using DataFrame.query(), query eg 'Fee==25000' method extract column values.
def dfQuery(df,query,displayColumn):
    df2=df.query()[displayColumn]
    print(df2.head())
    
# Check unique values of another column where any other column values are blank
def fetchColValForAnotherColBlank(df,col):
    tempDF3 = df.replace(' ', np.nan)                   # to get rid of empty values
    nan_values = tempDF3[tempDF3.isna().any(axis=1)]         # to get all rows with Na
    nan_values[col].value_counts()
#check missing Data (.isnull(),notnull())
def displayMissingData(df):
    missing_data = df.isnull()
    missing_data.head(5)
    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")   
# drop a record which has missing value
def dropARow(df,col):
    # simply drop whole row
    df.dropna(subset=[col], axis=0, inplace=True)
    # reset index
    df.reset_index(drop=True, inplace=True)
    print("**Done**")

    
# creating a function for splitting datetime into multiple features
def splitDate(df):        
    #Create time series features based on time series index.
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

def joinDate(df,year,month,day):
    #Join year month day in YYYY-MM-DD format.
    cols=[year,month,day]
    df['date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
    return df


def outlierRemovalUsingBoxPlot(df,col):
    ''' outlier Detection '''
    
        # IQR
    Q1 = np.percentile(df[col], 25,interpolation = 'midpoint')

    Q3 = np.percentile(df[col], 75,interpolation = 'midpoint')
    IQR = Q3 - Q1
    
    # Above Upper bound
    upper = df[col] >= (Q3+1.5*IQR)

#     print("Upper bound:",upper)
#     print(np.where(upper))

    # Below Lower bound
    lower = df[col] <= (Q1-1.5*IQR)
#     print("Lower bound:", lower)
#     print(np.where(lower))


#     "Old Shape: ", df.shape

    # Upper bound
    upper = np.where(df[col] >= (Q3+1.5*IQR))
    # Lower bound
    lower = np.where(df[col] <= (Q1-1.5*IQR))

    #Removing the Outliers
    df.drop(upper[0],axis=1,inplace=True)
    df.drop(lower[0],axis=1,inplace=True)
    
#     df.drop(upper[0],inplace=True)
#     df.drop(lower[0],inplace=True)
#     df = df.reset_index(drop=True)
#     "New Shape: ", df.shape
    return df
