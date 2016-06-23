from memory_profiler import profile
import pandas as pd

@profile
def main():
    data = pd.read_csv('data/info_train_top12.csv')
    x = data.values
    print x.shape


if __name__ == '__main__':
    main()
