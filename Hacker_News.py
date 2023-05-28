import csv
import requests


def artical_data(num):
   response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
   if response.status_code == 200:
      artical_list_id = response.json()
      dict_list = []
      for i in range(num):
         dict_list.append(requests.get(f'https://hacker-news.firebaseio.com/v0/item/{artical_list_id[i]}.json?print=pretty').json())
      return dict_list
   else:
      print ('ERROR')
   
   
def hacker_news(file_name,num):
   data_list = artical_data(num)
   with open(f"{file_name}.csv", 'w') as data_file:
      fieldnames = data_list[0].keys()
      writer = csv.DictWriter(data_file, fieldnames = fieldnames, extrasaction = 'ignore')
      writer.writeheader()
      writer.writerows(data_list)

   
hacker_news(input("enter the name for a csv file:\n"),int(input("number of articals:\n")))
