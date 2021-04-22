import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':1, 'job':2, 'marital':3,'education':4,'default':5 ,
'housing':6 ,'loan':7 ,'contact':8 ,'month':9 ,'day_of_week':10,
'duration':11,'campaign':12, 'pdays':13, 'previous':14,'poutcome':15, 'emp_var_rate':16, 
 'cons_price_idx':17, 'cons_conf_idx':18, 'euirboe3m':19, 'nr_employed':20, 'y':21 })

print(r.json())



  
