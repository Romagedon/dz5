number_of_persons = 4
ticket = 500
taxi = 600
number_of_pizzas = 2
pizza = 250
airhockey_rounds = 2
cost_of_airhockey_rounds = 80

cost_of_tickets = ticket * number_of_persons
cost_of_taxi = taxi + (taxi / 100 * 120)
cost_of_pizza = (pizza / 100 * 85) * number_of_pizzas
cost_of_airhockey = airhockey_rounds * cost_of_airhockey_rounds

result = (cost_of_taxi + cost_of_pizza + cost_of_airhockey + cost_of_tickets) / number_of_persons

print(f'{result = }')
