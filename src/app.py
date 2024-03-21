import pandas as pd
import sys
import os
from openpyxl import Workbook,load_workbook
import configparser
import json
import functions as fs
import writer as w


def getResourcePath(relativePath):
    return os.path.join(os.path.dirname(sys.argv[0]),"resource",relativePath)



if __name__=='__main__':
    #configを読み込む
    config=configparser.ConfigParser()
    config.read(getResourcePath('config.ini'))

    #シナリオのJsonを読み込む
    with open(getResourcePath('sample.json')) as j:
        scenario=json.load(j)
        #入力チェック TODO

        
    #必要あればS3から対象を取得
    #TODO

    #集計対象を読み込み、集計
    #TODO メモリ圧迫するので要改善（del、GCクリアなど含め）
    df=dict()
    for input in scenario['resource']['input'].items():
        df[input[0]]=pd.read_excel(getResourcePath(input[1]))

    
    datas=dict()
    for func in scenario['function']:
        tempdf=df.get(func['input'])
        for f in func['actions']:
            tempdf=fs.toFunc(f.get('command'))(tempdf,f.get('arg'))

        datas[func['name']]=tempdf
    
    #テンプレートを読み込む
    wb=load_workbook(filename=getResourcePath(scenario['resource']['template']))
    ws=wb.active

    #指定のセルに集計結果を書き込む
    w.setByOrigin(ws,"C5",datas.get('function1'))

    #別名で保存
    wb.save(scenario['resource']['output'])
