from fastapi import FastAPI
import pandas as pd
import uvicorn
from pandas import DataFrame,Series
from pydantic import BaseModel
from  typing import Optional,List,Dict
import os
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

app=FastAPI()

class PredictionInput(BaseModel):
    Length:float
    Diameter:float
    Height:float
    Weight:float
    Shucked_Weight:float
    Viscera_Weight:float
    Shell_Weight:float
    Sex:str

    
def load_model_pipe():
    cwd=os.getcwd()
    pipe_destination=os.path.join(cwd,"Notebooks and Pipelines","Pipelines")
    #cat_pipe_des=os.path.join(pipe_destination,"Categorical_pipe.joblib")
    #num_pipe_des=os.path.join(pipe_destination,"Numerical_pipe.joblib")
    #model_des=os.path.join(pipe_destination,"rsxgb_reg.joblib")
    model_dest=os.path.join(pipe_destination,"model.joblib")
    #cat_pipe=joblib.load(cat_pipe_des)
    #num_pipe=joblib.load(num_pipe_des)
    model=joblib.load(model_dest)

    return model#cat_pipe,num_pipe,model

"""def dataprocessing(datain,cat_pipe,num_pipe):
    df_crab=datain
    num_cols=[col for col in df_crab.columns if df_crab[col].dtype != "object"]
    cat_cols=[col for col in df_crab.columns if df_crab[col].dtype == "object"]
    df_crab[num_cols]=num_pipe.transform(df_crab[num_cols])
    df_crab[cat_cols]=cat_pipe.transform(df_crab[cat_cols])
    #col_trans=ColumnTransformer([("nums",num_pipe,num_cols),("cats",cat_pipe,cat_cols)])

    return df_crab"""

@app.get('/')
async def home():
    return {'message':'fast api home'}



@app.post("/prediction")
async def prediction(datain:PredictionInput):
    datain=DataFrame([datain.dict().values()],columns=datain.dict().keys())
    model=load_model_pipe()
    #cat_pipe,num_pipe,model=load_model_pipe()
    #data_df=dataprocessing(datain,cat_pipe,num_pipe)
    #model_steps=Pipeline([('cols_trans',col_trans),('model',model)])
    pred_val=model.predict(datain)
    return{"Predicted age is":int(pred_val)}


if __name__=="__main__":
    uvicorn.run("md_main:app",host="0.0.0.0",port=5000,reload=True)
















