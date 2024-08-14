import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
  def __init__(self):
    pass
    
  def predict(self,features):
    try:
      model_path = 'artifacts/model.pkl'
      preprocessor_path = 'artifacts/preprocessor.pkl'
      model = load_object(model_path)
      preprocessor = load_object(preprocessor_path)
      data_scaled = preprocessor.transform(features)
      preds = model.predict(data_scaled)
      return preds
    except Exception as e:  
      raise CustomException(e,sys)
    
class CustomData:
  def __init__(self,
               crop:str,
               season:str,
               state:str,
               area:int,
               production:int,
               rainfall:int,
               fertilizer:int,
               pesticide:int):
    
    self.crop = crop
    self.season = season
    self.state = state
    self.area = area
    self.production = production
    self.rainfall = rainfall
    self.fertilizer = fertilizer
    self.pesticide = pesticide
    
  def get_data_as_frame(self):
    try:
      custom_data_input_dict={
        "Crop":[self.crop],
        "Season":[self.season],
        "State":[self.state],
        "Area":[self.area],
        "Production":[self.production],
        "Annual_Rainfall":[self.rainfall],
        "Fertilizer":[self.fertilizer],
        "Pesticide":[self.pesticide]
      }
      
      return pd.DataFrame(custom_data_input_dict)
    
    except Exception as e:
      raise CustomException(e,sys)