import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from typing import Optional
import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.compose import ColumnTransformer

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

class PredictionOutput(BaseModel):
    Age:int


def load_pipes():
    cwd=os.getcwd()
    pipe_dest=os.path.join(cwd,"Notebooks and Pipelines","Pipelines")
    num_dest=os.path.join(pipe_dest,"Numerical_pipe.joblib")
    cat_dest=os.path.join(pipe_dest,"Categorical_pipe.joblib")
    num_pipe=joblib.load(num_dest)
    cat_pipe=joblib.load(cat_dest)

    return cat_pipe,num_pipe

def load_model():
    cwd=os.getcwd()
    pipe_dest=os.path.join(cwd,"Notebooks and Pipelines","Pipelines")
    model_dest=os.path.join(pipe_dest,"rsxgb_reg.joblib")
    model=joblib.load(model_dest)

    return model

def preprocess_input_data(data:PredictionInput,num_pipe,cat_pipe):
    df = pd.DataFrame([data.values()],columns=data.keys())
    num_cols=[col for col in df if df[col].dtype != 'object' ]
    cat_cols=[col for col in df if df[col].dtype = 'object' ]
    num_imput=num_pipe.transform(df[num_cols])
    cat_imput=cat_pipe.transform(df[cat_cols])
    col_trans=ColumnTransformer([("num",num_pipe,)])
    









