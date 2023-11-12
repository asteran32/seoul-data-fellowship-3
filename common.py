import os
import cv2
import numpy as np

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    '''Read images'''
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None
    
def imwrite(filename, img, params=None):
    '''Write image'''
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
def save_dataframe_to_excel(df, xlsx_path:str):
    '''Save output to xlsx'''
    df.to_excel(xlsx_path, index=False, engine='xlsxwriter')
    print(f'Saved {xlsx_path}')