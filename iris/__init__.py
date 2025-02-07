import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame


def get_iris_data():
    iris_set = []
    with open("../data/iris.data") as dataset:
        for line in dataset:
            iris_set.append(line.strip())
    return iris_set

def clean_data_frame(data_set: []):
    cleaned = separate_variables(data_set)
    df = pd.DataFrame(data=cleaned, columns=['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])
    return df


def separate_variables(iris_set: [str]) -> list[list[str]]:
    cleaned = []
    for line in iris_set:
        line = line.split(",")
        cleaned.append(line)
    return cleaned


def main():
    iris_set = get_iris_data()
    cleaned = clean_data_frame(iris_set)

    # plt.hist(cleaned)
    # plt.show()

main()