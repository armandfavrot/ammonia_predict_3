import torch

def generate_tensors_predictors(df, pmid, device):
    
    data_filtered = df[df['pmid'] == pmid]

    x_cont = data_filtered[['ct', 'dt', 'air_temp', 'wind_2m', 'rain_rate', 'tan_app', 'app_rate', 'man_dm', 'man_ph', 't_incorp']]

    x_cont_tensor = torch.tensor(x_cont.values, dtype=torch.float32).view(len(x_cont), len(x_cont.columns))
    x_cont_tensor = x_cont_tensor.to(device)
    
    x_cat = data_filtered[['app_mthd', 'incorp', 'man_source']]
    
    x_cat_tensor = torch.tensor(x_cat.values, dtype=torch.long).view(len(x_cat), len(x_cat.columns))
    x_cat_tensor = x_cat_tensor.to(device)
    x_cat_tensor = torch.unbind (x_cat_tensor, dim = 1)

    output = [x_cont_tensor, x_cat_tensor]
    
    return output
