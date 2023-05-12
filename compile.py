import csv;
import json;
import os;

from shutil import rmtree

name = "create-potion-buckets"
recipe_path = f"./data/{name}/recipes"

# This value was determine by recipes within the bucket subtype.
# However, the value proportions between a bottle and bucket for potions is equivalent to 1 to 2.5, rather than the expected 1 to 4.
amount = 1000

if os.path.exists(recipe_path):
		rmtree(recipe_path)

def potion_bucket(id: str):
	return {
		"item": "tconstruct:potion_bucket",
		"nbt": {
			"Potion": f"minecraft:{id}"
		}
	}

def potion_fluid(id: str, amount: int):
	return {
		"fluid": "create:potion",
		"nbt": {
			"Bottle": "REGULAR",
			"Potion": f"minecraft:{id}"
		},
		"amount": amount
	}

def gen_emptying_recipe(id: str):
	return {
		"type": "create:emptying",
		"ingredients": [
			potion_bucket(id)
		],
		"results": [
			{
				"item": "minecraft:bucket"
			},
			potion_fluid(id, amount)
		]
	}

def gen_filling_recipe(id: str):
	return {
		"type": "create:filling",
		"ingredients": [
			{
				"item": "minecraft:bucket"
			},
			potion_fluid(id, amount)
		],
		"results": [
			potion_bucket(id)
		]
	}

os.mkdir(recipe_path)
os.mkdir(recipe_path + "/emptying")
os.mkdir(recipe_path + "/filling")

with open("./potions.csv") as file:
	file.readline() # skip header
	reader = csv.reader(file.readlines())

for row in reader:
	id = row[0]

	with open(f"{recipe_path}/emptying/{id}_bucket.json", "x") as emptying_file:
		recipe = json.dumps(gen_emptying_recipe(id), indent=4)
		emptying_file.write(recipe)

	with open(f"{recipe_path}/filling/{id}_bucket.json", "x") as filling_file:
		recipe = json.dumps(gen_filling_recipe(id), indent=4)
		filling_file.write(recipe)


