from utils.model import Perceptron
from utils.all_utils import prepare_data,save_model,save_plot
import pandas as pd
print(pd.__version__)
import numpy as np
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=logging_str)


def main(data,eta,epochs,filename,plotfilename):
    df = pd.DataFrame(data)
    print(f"This is actual dataframe{df}")
    X,y = prepare_data(df)
    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)
    _ = model.total_loss()


    save_model(model, filename=filename)
    save_plot(df, plotfilename, model)

if __name__ == '__main__':
    AND = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,0,0,1],
    }
    ETA = 0.3 # 0 and 1
    EPOCHS = 10
    main(data=AND,eta = ETA,epochs=EPOCHS,filename="and.model",plotfilename= "and.png")