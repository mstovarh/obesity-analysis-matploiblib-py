import read_csv
import charts 

#Funcion de conteo por categorias
def count_categories(data):
  weight_counts = {}

  for item in data:
    weight_category = item['NObeyesdad']
    #print(weight_category)
    weight_counts[weight_category] = weight_counts.get(weight_category, 0) + 1
    #print(weight_counts)

  weight_type = list(weight_counts.keys()) 
  recuento = list(weight_counts.values()) 
  return weight_type, recuento

#Funciones de conteo por categorias
def get_Char1():
  data = read_csv.read_csv('obesity_gen.csv')
  data = list(filter(lambda item : item['Gender'] == 'Female', data))
  (weight_type, recuento) = count_categories(data)
  charts.generate_bar_chart(weight_type, recuento, 'Estados de peso corporal en mujeres', 'chart1')

def get_Char2():
  data = read_csv.read_csv('obesity_gen.csv')
  data = list(filter(lambda item : item['Gender'] == 'Male', data))
  (weight_type, recuento) = count_categories(data)
  charts.generate_bar_chart(weight_type, recuento, 'Estados de peso corporal en hombres', 'chart2')

def get_Char3():
  data = read_csv.read_csv('obesity_gen.csv')
  data = list(filter(lambda item : item['Gender'] == 'Female' and (int(item['Age']) > 40 and int(item['Age']) < 60), data))
  (weight_type, recuento) = count_categories(data)
  charts.generate_bar_chart(weight_type, recuento, 'Estados de peso corporal en mujeres entre 40 y 60 años', 'chart3')

def get_Char4():
  data = read_csv.read_csv('obesity_gen.csv')
  data = list(filter(lambda item : item['Gender'] == 'Male' and (int(item['Age']) > 40 and int(item['Age']) < 60), data))
  (weight_type, recuento) = count_categories(data)
  charts.generate_bar_chart(weight_type, recuento, 'Estados de peso corporal en hombres entre 40 y 60 años', 'chart4')

if __name__ == '__main__':
  get_Char1()
  get_Char2()
  get_Char3()
  get_Char4()