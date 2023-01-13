import pandas as pd

data = {
    "apples": [3,4,6,9],
    "oranges":[1,5,6,8]
}

# purchases = pd.DataFrame(data)

index = ['Aron','lee','steve','Shaun']
purchases = pd.DataFrame(
    data,index=index
)
print(purchases)
print(type(purchases))

# print(purchases["apples"])  # Extract a single column

print(purchases.loc['Aron']) # Extract a specific row
