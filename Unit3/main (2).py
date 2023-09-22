#Here we write a function linear search product that lists product and target product and do the tasks which given in challenge.

def LinearSearchProduct(productList, targetproduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)

  return indices

#Lets check the code with Example
products = ["shoes","boot","loafer","shoes","sandal","shoes","boot","shoes"]
target = "shoes"
target2 = 'apple'
result = LinearSearchProduct(products,target)
print(result)
print("\nLinear Search Performed")