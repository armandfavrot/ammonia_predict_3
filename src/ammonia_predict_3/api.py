import pandas as pd
import torch
import torch.nn as nn
from importlib.resources import files, as_file


from .model_def import AmmoniaRNN
from .utils import generate_tensors_predictors


DEVICE = "cpu"
num_layers = 1
nonlinearity = "relu"
bidirectional = True
hidden_size = 512 

cat_dims = [5, 3, 2]  
embedding_dims = [10, 9, 8]  
input_size = 13   
output_size = 1

model = AmmoniaRNN(input_size = input_size, 
                   output_size = output_size, 
                   hidden_size = hidden_size, 
                   nonlinearity = nonlinearity,
                   num_layers = num_layers,
                   bidirectional = bidirectional,
                   cat_dims = cat_dims, 
                   embedding_dims = embedding_dims).to(DEVICE)


resource = files(__package__) / "data" / "final_model.pth"
with as_file(resource) as path:
    model.load_state_dict(torch.load(str(path), weights_only = True, map_location=torch.device('cpu')))


def predict (df):

    data_predictions = df.copy()

    pmids = data_predictions['pmid'].unique()
    
    data_predictions['prediction_ecum'] = None
    data_predictions['prediction_delta_ecum'] = None
        
    with torch.no_grad():
    
        all_predictions = torch.empty(0).to(DEVICE)
    
            
        for i in pmids:
    
            x = generate_tensors_predictors (data_predictions, i, device = DEVICE)
            y = model(x)
            all_predictions = torch.cat ((all_predictions, y.squeeze()), 0)
    
        data_predictions['prediction_delta_ecum'] = all_predictions.to("cpu").detach()
    
    data_predictions['prediction_ecum'] = data_predictions.groupby('pmid')['prediction_delta_ecum'].cumsum()

    return data_predictions
