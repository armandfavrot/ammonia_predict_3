import pandas as pd
from ammonia_predict_3 import predict

def test_predict_columns():
    df = pd.DataFrame({
        "pmid": [1, 1, 2, 2],
        "ct": [2, 4, 2, 4],
        "dt": [2, 2, 2, 2],
        "air_temp": [12, 15, 11, 10],
        "wind_2m": [3, 3, 4, 2],
        "rain_rate": [0, 0, 1, 0],
        "tan_app": [36.7, 36.7, 36.7, 36.7],
        "app_rate": [10, 10, 12, 12],
        "man_dm": [0.1, 0.1, 0.1, 0.1],
        "man_ph": [7, 7, 7, 7],
        "t_incorp": [0, 0, 0, 0],
        "app_mthd": [1, 1, 1, 1],
        "incorp": [0, 0, 0, 0],
        "man_source": [1, 1, 1, 1],
    })

    out = predict(df)
    assert "prediction_delta_ecum" in out.columns
    assert "prediction_ecum" in out.columns
    assert len(out) == len(df)
