from memory_profiler import profile
from numpy import genfromtxt

@profile
def main():
    data = genfromtxt('data/info_train_top12.csv', delimiter=',')
    x = data.copy()
    print x.shape


if __name__ == '__main__':
    main()
