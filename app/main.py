import utils
import rcsv
import charts

def run():
  data = rcsv.read_csv('./app/data.csv')
  data =list(filter(lambda el:el['Continent']== 'South America',data))
  #print (data)
  
  countries = utils.get_col(data,'CCA3')
  #porcentages = input('Enter the column that you want obtein ==>')
  #porcentages = porcentages.capitalize()
  porcentages = utils.get_col(data,'World Population Percentage')
  
  #print(porcentages, countries)
  charts.generate_pie_chart(countries,porcentages)
  
if __name__ == '__main__':
  run()