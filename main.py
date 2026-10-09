import csv 


with open("data/customers.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        customers = {'customer_id': row['customer_id'], 'name': row['name'], 'city': row['city'], 
                'age': int(row['age'])      }
        
        print(customers)





