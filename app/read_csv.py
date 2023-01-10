import csv
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []                     # versión 4, crea el data para poder devolver su valor
    for row in reader:
      iterable = zip(header,row)   # versión 2                    crea iterable, duplas header, valor
      country_dict = {key: value for key, value in iterable}    # versión 3 diccionario
      data.append(country_dict)                                 #  versión 4
  return data                                                   # versión 4
      
 
 
if __name__ == '__main__':
#  read_csv('./app/data.csv')         versión inicial
  data = read_csv('./app/data.csv')
  print(data[0])           
                   