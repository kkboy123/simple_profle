from memory_profiler import profile
import csv

@profile
def main():
    with open('data/info_train_top12.csv') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        print len(data), len(data[0])
        print 1


if __name__ == '__main__':
    main()
