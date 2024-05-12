from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
nursery = fetch_ucirepo(id=76) 
  
# data (as pandas dataframes) 
X = nursery.data.features 
y = nursery.data.targets 
  
# metadata 
print(nursery.metadata) 
  
# variable information 
print(nursery.variables) 
