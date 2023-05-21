
def get_pet_shop_name(pet_shop):
	return pet_shop["name"]

def get_total_cash(pet_shop):
	return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
	pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
	return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
	pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
	return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
	return [p for p in pet_shop["pets"] if p["breed"] == breed]

def find_pet_by_name(pet_shop, name):
	for p in pet_shop["pets"]:
		if p["name"] == name:
			return p
	return None

def remove_pet_by_name(pet_shop, name):
	for p in pet_shop["pets"][:]:		# iterate over copy of list
		if p["name"] == name:
			pet_shop["pets"].remove(p)	# remove from original

def add_pet_to_stock(pet_shop, new_pet):
	pet_shop["pets"].append(new_pet)
	
def get_customer_cash(customer):
	return customer["cash"]
	
def remove_customer_cash(customer, amount):
	customer["cash"] -= amount
	
def get_customer_pet_count(customer):
	return len(customer["pets"])
	
def add_pet_to_customer(customer, pet):
	customer["pets"].append(pet)
	
def customer_can_afford_pet(customer, pet):
	return True	if customer["cash"] >= pet["price"] else False

def sell_pet_to_customer(pet_shop, pet, customer):
	if pet is not None:
		if find_pet_by_name(pet_shop, pet["name"]):
			if customer_can_afford_pet(customer, pet):
				remove_customer_cash(customer, pet["price"])
				add_pet_to_customer(customer, pet)
				remove_pet_by_name(pet_shop, pet["name"])
				add_or_remove_cash(pet_shop, pet["price"])
				increase_pets_sold(pet_shop, 1)
