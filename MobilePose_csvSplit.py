import numpy as np
import csv


all_data = open("./dataset/data.csv").readlines()
N = len(all_data)
N_test = int(N * 0.1)
N_train = N - N_test

print('N:{}'.format(N))
print('N_train:{}'.format(N_train))
print('N_test:{}'.format(N_test))

np.random.seed(1701)
perm = np.random.permutation(N)
test_indices = perm[:N_test]
train_indices = perm[N_test:]

print('train_indices:{}'.format(len(train_indices)))
print('test_indices:{}'.format(len(test_indices)))

with open('./dataset/test_data.csv',newline='',mode='w') as data_csv:
    data_writer = csv.writer(data_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
    for i in test_indices:
        line=all_data[i].split(",")
        filename=line[0]
        for j in range(len(line)):
            if j!=0 and j!=(len(line)-1):
                line[j]=float(line[j])
            if j==len(line)-1:
                line[len(line)-1]=line[len(line)-1][:-1]
                line[len(line)-1]=float(line[len(line)-1])
        data_writer.writerow(line)
        print(line)

with open('./dataset/train_data.csv',newline='',mode='w') as data_csv:
    data_writer = csv.writer(data_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
    for i in train_indices:
        line=all_data[i].split(",")
        filename=line[0]
        for j in range(len(line)):
            if j!=0 and j!=(len(line)-1):
                line[j]=float(line[j])
            if j==len(line)-1:
                line[len(line)-1]=line[len(line)-1][:-1]
                line[len(line)-1]=float(line[len(line)-1])
        data_writer.writerow(line)
        print(line)