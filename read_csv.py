import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';') 
        header = next(reader)
        #print(header)
        obesity = []
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable))
            obesity_dict = dict(iterable)
            #obesity_dict = {key: value for key, value in iterable}
            #print(obesity_dict)
            obesity.append(obesity_dict)
        return obesity

                  
if __name__ == '__main__':
    obesity = read_csv('./obesity/obesity_gen.csv')
    print(obesity)