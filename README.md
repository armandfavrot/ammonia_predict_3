# ammonia-predict

Ce package consiste en une unique fonction 'predict' qui permet de prédire les émissions d'ammoniac suite à la fertilisation des champs en fonction de certaines conditions environnementales. Le modèle utilisé est un réseau de neurones récurrent qui est décrit dans [ref] sour le nom de 'rnn 9 - data a.'. La fonction 'predict' fonctionne de manière similaire à fonction 'alfam2' du package r ALFAM2 disponible [ici](https://cran.r-project.org/web/packages/ALFAM2/index.html).

## Install

```bash
pip install nh3pred 
```

## Documentation

Une aide complète pour la fonction 'predict' est disponible ici.

## Usage

You can use the package in Python as follows:

```python
import pandas as pd
from ammonia_predict_3 import predict

df = pd.DataFrame ({
    "pmid": [1, 1, 1, 1, 1, 1],
    "ct": [3, 6, 10, 24, 48, 72],
    "tan_app": [42, 42, 42, 42, 42, 42],
    "air_temp": [18, 23, 24, 15, 21, 20],
    "wind_2m": [2, 2, 1, 1, 2, 2],
    "rain_rate": 0,
    "app_rate": [20, 20, 20, 20, 20, 20],
    "man_dm": [8.3, 8.3, 8.3, 8.3, 8.3, 8.3],
    "man_ph": [7.1, 7.1, 7.1, 7.1, 7.1, 7.1],
    "app_mthd": ["ts", "ts", "ts", "ts", "ts", "ts"],
    "man_source": ["cat", "cat", "cat", "cat", "cat", "cat"]
})

pred = predict(df)
print(pred)
``` 


## Notes

- The trained weights are included in the package under `ammonia_predict/data/final_model.pth`.
- The package requires **Python ≥3.9**, **PyTorch**, and **pandas**.



