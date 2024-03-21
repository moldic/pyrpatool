from pandas import DataFrame

def toFunc(func:str):
    if func=='query':
        return query
    elif func=='groupby':
        return groupby
    elif func=='size':
        return size
    else:
        return print

def query(df:DataFrame,arg:str=""):
    return df.query(arg)
    
def groupby(df:DataFrame,arg:str=""):
    return df.groupby(arg)
    
def size(df:DataFrame,arg):
    return df.size()
    