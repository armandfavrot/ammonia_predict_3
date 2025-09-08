# ammonia-predict

Predict ammonia emissions with a simple RNN model.

## Install (dev)

```bash
pip install -e .
```


## Usage

You can use the package in Python as follows:

```python
import pandas as pd
from ammonia_predict_3 import predict

df = pd.DataFrame({
    "pmid": [1, 1],
    "ct": [2, 4],
    "dt": [2, 2],
    "air_temp": [12, 15],
    "wind_2m": [3, 3],
    "rain_rate": [0, 0],
    "tan_app": [36.7, 36.7],
    "app_rate": [10, 10],
    "man_dm": [0.1, 0.1],
    "man_ph": [7, 7],
    "t_incorp": [0, 0],
    "app_mthd": [1, 1],
    "incorp": [0, 0],
    "man_source": [1, 1],
})

pred = predict(df)
print(pred[["prediction_delta_ecum", "prediction_ecum"]])
``` 


## Notes

- The trained weights are included in the package under `ammonia_predict/data/final_model.pth`.
- The package requires **Python ≥3.9**, **PyTorch**, and **pandas**.



