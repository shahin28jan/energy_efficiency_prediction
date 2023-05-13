import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
                    

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
       
        
class CustomData:
    def __init__(self,
                 relative_compactness:float,
                 surface_area:float,
                 wall_area:float,
                 roof_area:float,
                 overall_height:float,
                 glazing_area:float,
                 glazing_area_distribution:float):
        
        self.relative_compactness=relative_compactness
        self.surface_area=surface_area
        self.wall_area=wall_area
        self.roof_area=roof_area
        self.overall_height=overall_height
        self.glazing_area = glazing_area
        self.glazing_area_distribution = glazing_area_distribution
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'relative_compactness':[self.relative_compactness],
                'surface_area':[self.surface_area],
                'wall_area':[self.wall_area],
                'roof_area':[self.roof_area],
                'overall_height':[self.overall_height],
                'glazing_area':[self.glazing_area],
                'glazing_area_distribution':[self.glazing_area_distribution]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
