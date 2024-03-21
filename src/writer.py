from openpyxl.utils import cell

def setByOrigin(ws,origin,data):
    #TODO 範囲が広がった場合に行を拡張するオプション？

    origin_as_string=cell.coordinate_from_string(origin)
    origin_as_number=(cell.column_index_from_string(origin_as_string[0]),origin_as_string[1])
    for r,items in enumerate(data.items(),0):
        for i,item in enumerate(items,0):
            ws.cell(row=origin_as_number[1]+r,\
                    column=origin_as_number[0]+i,value=item) 

