# import packages
from fastapi import FastAPI,Header,HTTPException
import pandas as pd

# membuat instance/object
app = FastAPI()

secret="hactiv8jayajaya"


# endpoint -> aturan request dari client
# endpoint untuk menampilkan halaman utama
@app.get('/')
def getHome():
    # read data
    df = pd.read_csv('data.csv')

    # mengembalikan data ke client
    return {
        'data' : df.to_dict(orient='records')
    }

# endpoint untuk menampilkan data hasil filter (by name)
@app.get('/data/{filter}')
def getData(filter: str):
    # read data
    df = pd.read_csv('data.csv')

    # filter dataframe
    #result = df[df.name == filter]
    #return result.to_dict(orient='records')
    result = df.query(f"name == '{filter}'")
    return result.to_dict(orient='records')


# endpoint untuk menampilkan data hasil filter (by name)
#ex
@app.delete('/data/{filter}')
def deleteData(filter: str,api_key=Header(None)):
    if api_key is not None and api_key == secret:
        print("password benar")
    
    # read data
        df = pd.read_csv('data.csv')

    # filter dataframe
        result = df[df.name != filter]

    # replace data existing with filter
        result.to_csv('data.csv', index=False)

        return result.to_dict(orient='records')
    else:

        raise HTTPException(400,"password salah")
#else:
        #print("password salah")