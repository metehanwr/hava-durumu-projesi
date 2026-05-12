
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class ModelTrainer:
    def __init__(self, veri):
        self.veri  = veri
        self.model = None

    def egit_ve_degerlendir(self):

        X = self.veri[["nem", "ruzgar_hizi", "yagis", "basinc", "ay"]].values
        y = self.veri["sicaklik"].values


        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )


        scaler  = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test  = scaler.transform(X_test)


        self.model = MLPRegressor(
            hidden_layer_sizes=(64, 32),
            activation="relu",
            max_iter=1000,
            random_state=42
        )
        self.model.fit(X_train, y_train)


        tahmin = self.model.predict(X_test)
        mae  = round(mean_absolute_error(y_test, tahmin), 4)
        mse  = round(mean_squared_error(y_test, tahmin), 4)
        rmse = round(float(np.sqrt(mse)), 4)
        r2   = round(r2_score(y_test, tahmin), 4)

        print("\n--- Model Sonuçları (MLPRegressor) ---")
        print(f"  MAE  : {mae} °C")
        print(f"  MSE  : {mse}")
        print(f"  RMSE : {rmse} °C")
        print(f"  R²   : {r2}")

        return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}
