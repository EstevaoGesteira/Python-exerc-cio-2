nome_do_produto = input("Nome do produto: ")
quantidade_do_produto = int(input("Quantidade do produto:"))
preco_do_produto = float(input("Preço do produto: "))

total_comprado = quantidade_do_produto * preco_do_produto

print(f"O produto é: {nome_do_produto}")
print(f"A quantidade do produto é: {quantidade_do_produto}")
print(f"O preço unitário é: {preco_do_produto:.2f}")
print(f"O valor total é: {total_comprado:.2f}")