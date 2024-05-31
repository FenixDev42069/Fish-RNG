import random
import os
import time

InMenu = False
items = []

Dimention = "overworld"

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_items(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            file.write(item + '\n')

def load_items(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            items.append(line.strip())
    return items

def print_items(items):
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    
    for item, count in item_counts.items():
        if count > 1:
            print(f"{item} x{count}")
        else:
            print(item)

def print_items_with_indices(items):
	for index, item in enumerate(items):
		print(f"{index}: {item}")

def remove_items(items):
	print("Tus items:")
	print_items_with_indices(items)
	
	while True:
		try:
			indices_str = input("Escribe los números de índice de los items que quieres eliminar (separados por espacios): ")
			indices = sorted([int(idx) for idx in indices_str.split()], reverse=True)
			
			for idx in indices:
				if idx >= 0 and idx < len(items):
					del items[idx]
			
			save_items(items, 'items.txt')
			print("Items eliminados correctamente.")
			time.sleep(1.5)
			Clear()
			Menu()
			break
		except ValueError:
			print("Por favor, introduce números válidos.")
		except IndexError:
			print("Uno o más índices son inválidos. Inténtalo de nuevo.")
            
def get_item_counts(items):
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts

def check_items(items, item_name, quantity=1):
    item_counts = get_item_counts(items)
    if item_name in item_counts and item_counts[item_name] >= quantity:
        return True
    else:
        return False

#Llamada de ejemplo:
#check_items(items, "Legendario", 2)

def Del_i(items, item_name, num_to_remove=1):
    count_removed = 0
    while item_name in items and count_removed < num_to_remove:
        items.remove(item_name)
        count_removed += 1
    
    if count_removed > 0:
        save_items(items, 'items.txt')
        
    else:
        print(f"No se encontró el item '{item_name}' en el inventario o la cantidad a eliminar es mayor a la cantidad presente.")

#Llamada de ejemplo:
#remove_item_by_name(items, "Hades")

def Craft(items, material1, mat1amm, material2, mat2amm, output):
	item_counts = get_item_counts(items)
	if check_items(items, material1, mat1amm) and check_items(items, material2, mat2amm):
		Item = output
		items.append(Item)
		Del_i(items, material1, mat1amm)
		Del_i(items, material2, mat2amm)
		save_items(items, 'items.txt')
		print(f"El item '{Item}' ah sido creado correctamente y guardado al inventario")
		time.sleep(2)
		if MC:
			MCRFT()
		elif MainG:
			Menu()
	else:
		print("Error: Materiales insuficientes")
		time.sleep(2)
		if MC:
			MCRFT()
		elif MainG:
			Menu()

def MCRFT(dimention="overworld"):
	global MC
	global MainG
	
	MC = True
	MainG = False
	
	if dimention == "overworld":
		global bioma
		bioma = 0
		Clear()
		print(f"Dimension: {dimention}")
		print("")
		print("Acciones:")
		print("")
		print("N - Talar arbol")
		print("C - Craftear")
		if check_items(items, "Pico"):
			print("M - Minar")
		if check_items(items, "Multi-portal"):
			print("V - Cambiar de dimension")
		print("Q - Volver al menu")
		print("E - Inventario")
		print("")
		Accion = input(str(">>> ")).lower()
		if Accion == "n":
			Item = "Tronco"
			items.append(Item)
			save_items(Item, 'items.txt')
			print(f"Has obtenido '{Item}'")
			time.sleep(1.5)
			MCRFT()
		elif Accion == "c":
			Clear()
			print("Recetas:")
			print("")
			print("[1] Madera - Tronco + Tronco")
			print("[2] Palos - Madera + Tronco")
			print("[3] Cabeza de pico - Madera x2 + Madera")
			print("[4] Pico - Cabeza de pico + Palos")
			print("[5] Portal nether - Obsidiana x8 + Pedernal")
			print("[6] Portal end - Vacio + Portal nether")
			print("[7] Multi-portal - Portal end + Portal nether")
			print("")
			Crafting_2 = input(str(">>> ")).lower()
			if Crafting_2 == "1":
				Craft(items, "Tronco", 1, "Tronco", 1, "Madera")
			elif Crafting_2 == "2":
				Craft(items, "Madera", 1, "Tronco", 1, "Palos")
			elif Crafting_2 == "3":
				Craft(items, "Madera", 2, "Madera", 1, "Cabeza de pico")
			elif Crafting_2 == "4":
				Craft(items, "Cabeza de pico", 1, "Palos", 1, "Pico")
			elif Crafting_2 == "5":
				Craft(items, "Obsidiana", 8, "Pedernal", 1, "Portal nether")
			elif Crafting_2 == "6":
				Craft(items, "Vacio", 1, "Portal nether", 1, "Portal end")
			elif Crafting_2 == "7":
				Craft(items, "Portal end", 1, "Portal nether", 1, "Multi-portal")
		elif Accion == "m":
			Ore = random.randint(1,20)
			if Ore <= 1:
				print("Minando el vacio...")
				time.sleep(10)
				Item = "Vacio"
			elif Ore <= 3:
				print("Minando diamantes...")
				time.sleep(3)
				Item = "Diamante"
			elif Ore <= 9:
				print("Minando obsidiana...")
				time.sleep(5.5)
				Item = "Obsidiana"
			elif Ore <= 12:
				print("Minando grava...")
				Grava = random.randint(1,5)
				time.sleep(1.5)
				if Grava == 1:
					Item = "Pedernal"
				else:
					Item = "Grava"
			elif Ore <= 20:
				print("Minando cobblestone...")
				time.sleep(1)
				Item = "Cobblestone"
			
			while True:
				decision = input(str("Deseas guardar el item? [Y/N]:")).lower()
				if decision == "y":
					items.append(Item)
					save_items(items, 'items.txt')
					print(f"'{Item}' guardado")
					time.sleep(1)
					MCRFT()
					break
				elif decision == "n":
					print("Item descartado")
					time.sleep(1)
					MCRFT()
					break
		elif Accion == "q":
			print("Volviendo al menu...")
			time.sleep(1)
			Menu()
		elif Accion == "e":
			print("")
			print_items(items)
			print("")
			input("Presiona ENTER para continuar...")
			MCRFT()
		elif Accion == "v":
			Clear()
			print("Viajando al nether...")
			time.sleep(2.5)
			MCRFT("nether")
		else:
			print("Error, accion no reconocida")
			time.sleep(1)
			MCRFT()

	elif dimention == "nether":
		Clear()
		if bioma == 0:
			bioma = random.randint(1,3)
		if bioma == 1:
			Bioma = "Nether wastes"
		elif bioma == 2:
			Bioma = "Basalt deltas"
		else:
			Bioma = "Warped forest"
		print(f"Dimension: {dimention}")
		print(f"Bioma: {Bioma}")
		print("")
		print("Acciones:")
		print("")
		print("N - Explorar")
		print("C - Craftear")
		print("M - minar")
		print("V - Cambiar de dimension")
		print("Q - Volver al menu")
		print("E - Inventario")
		print("")
		Accion = input(str(">>> ")).lower()
		if Accion == "n":
			bioma = random.randint(1, 3)
			if bioma == 1:
				Bioma = "Nether wastes"
			elif bioma == 2:
				Bioma = "Basalt deltas"
			else:
				Bioma = "Warped forest"
			print("Explorando...")
			time.sleep(5)
			print(f"Has llegado al {Bioma}")
			time.sleep(1.5)
			MCRFT("nether")
		elif Accion == "c":
			Clear()
			print("[1] Balde de piedra - Cobblestone x4 + pedernal")
			print("[2] Lingote de oro - Ore dorado + Ore dorado")
			print("[3] Netherite - Lingote de oro x4 + Acient debris x4")
			print("[4] Oro fundido - Balde de lava + Lingote de oro x3")
			print("[5] Bloque de netherite - Netherite x4 + Netherite x4")
			print("[6] Bloque de la fortuna - Bloque de netherite + Oro fundido")
			print("")
			Crafting = input(str(">>> "))
			if Crafting == "1":
				Craft(items, "Cobblestone", 4, "Pedernal", 1, "Balde de piedra")
			elif Crafting == "2":
				Craft(items, "Ore dorado", 1, "Ore dorado", 1, "Lingote de oro")
			elif Crafting == "3":
				Craft(items, "Lingote de oro", 4, "Ancient debris", 4, "Netherite")
			elif Crafting == "4":
				Craft(items, "Balde de lava", 1, "Lingote de oro", 3, "Oro fundido")
			elif Crafting == "5":
				Craft(items, "Netherite", 4, "Netherite", 4, "Bloque de netherite")
			elif Crafting == "6":
				Craft(items, "Bloque de netherite", 1, "Oro fundido", 1, "Bloque de la fortuna")
			else:
				print("Error, no se reconoce la id")
				time.sleep(1.5)
				MCRFT("nether")
		elif Accion == "m":
			Ore = random.randint(1,10)
			Lava = random.randint(1, 4)
			if Ore <= 1:
				Item = "Ancient debris"
				print(f"Minando {Item}...")
				time.sleep(2)
			elif Ore <= 4:
				Item = "Ore dorado"
				print(f"Minando {Item}...")
				time.sleep(1.2)
			elif Ore <= 10:
				if Lava == 1 and check_items(items, "Balde de piedra"):
					Item = "Balde de lava"
					Del_i(items, "Balde de piedra")
					print(f"Consiguiendo un {Item}...")
					time.sleep(0.5)
				else:
					Item = "Netherack"
					print(f"Minando {Item}...")
					time.sleep(0.8)
			
			while True:
				decision = input(str("Deseas guardar el item? [Y/N]:")).lower()
				if decision == "y":
					items.append(Item)
					save_items(items, 'items.txt')
					print(f"'{Item}' guardado")
					time.sleep(1)
					MCRFT("nether")
					break
				elif decision == "n":
					print("Item descartado")
					time.sleep(1)
					MCRFT("nether")
					break
					
		elif Accion == "v":
			Clear()
			print("Viajando al end...")
			time.sleep(2.5)
			MCRFT("end")
		elif Accion == "q":
			print("Volviendo al menu...")
			time.sleep(1)
			Menu()
		elif Accion == "e":
			print("")
			print_items(items)
			print("")
			input("Presiona ENTER para continuar...")
			MCRFT("nether")
		else:
			print("Comando no reconocido")
			time.sleep(1.5)
			MCRFT("nether")

	elif dimention == "end":
		Clear()
		print(f"Dimension: {dimention}")
		print("")
		print("Acciones:")
		print("")
		if not check_items(items, "Huevo de dragon"):
			print("N - Matar al dragon (Requiere OP)")
		print("C - Craftear")
		print("V - Cambiar de dimension")
		print("")
		Accion = input(str(">>> ")).lower()
		if Accion == "n":
			if check_items(items, "OP"):
				print("Muere dragon!!")
				time.sleep(2)
				Item = "Huevo de dragon"
				items.append(Item)
				save_items(Item, 'items.txt')
				print(f"Has matado al dragon y obtenido {Item}, Felicidades!")
				Item = "Medalla"
				items.append(Item)
				save_items(Item, 'items.txt')
				time.sleep(5)
				MCRFT("end")
			else:
				print("Error: no tienes el item requerido (OP)")
		elif Accion == "v":
			print("Viajando al overworld...")
			time.sleep(2.5)
			MCRFT()
		elif Accion == "c":
			Clear()
			print("Crafteos:")
			print("")
			print("[1] Bloque de comandos - Bloque de la fortuna + Legendario")
			print("[2] OP - Bloque de comandos + La ostia")
			print("[3] Dragon gem - Huevo de dragon + ¿¿¿???")
			print("")
			Crafting = input(str(">>> "))
			if Crafting == "1":
				Craft(items, "Bloque de la fortuna", 1, "Legendario", 1, "Bloque de comandos")
			elif Crafting == "2":
				Craft(items, "Bloque de comandos", 1, "La ostia (Epico)", 1, "OP")
			elif Crafting == "3":
				Craft(items, "Huevo de dragon", 1, "Mitico", 1, "Dragon gem")
			else:
				print("Error: id no reconocida")
				time.sleep(1.5)
				MCRFT("end")

def Roll():
    global InMenu
    Rolling = False
    
    if not Rolling:
        Rolled = random.randint(1, 10000000)
        Rolled_2 = random.randint(1, 10)
        Rolled_3 = random.randint(1, 100)
        Rolling = True
       
        if Rolled == 1:
        	if Rolled_2 and Rolled_3 == 1:
        		Item = "Ī̷̝̭̱m̴͚̭͋͑́̐p̶͖̅̎ö̶̠̹́̎̉͆̀ͅs̷̘̗͌i̴̘̘̽́͠b̵̧̫͈̬̝͋̔̈́l̸̦̥̆̇̇̈́́e̶̡̯̪͖̓̌̉̈́͘"
        	else:
        		Item = "Unreal"
        elif Rolled <= 10:
        	if Rolled_2 <= 2:
        		Item = "Hades"
        	elif Rolled_2 <= 4:
        		Item = "Zeus"
        	elif Rolled_2 <= 6:
        		Item = "Athenas"
        	elif Rolled_2 <= 8:
        		Item = "Juno"
        	else:
        		Item = "Venus"
        if Rolled <= 777:
        	if Rolled_2 >= 5:
        		Item = "Fortune"
        	else:
        		Item = "Vegetta"
        if Rolled <= 1000:
        	if Rolled_2 >= 5:
        		Item = "Ying"
        	else:
        		Item = "Yang"
        if Rolled <= 10000:
        	if Rolled_3 and Rolled_2 == 1:
        		Item = "Godly (Mitico)"
        	else:
        		Item = "Mitico"
        if Rolled <= 100000:
        	if Rolled_3 == 1:
        		Item = "Pou (Legendario)"
        	else:
        		Item = "Legendario" 
        elif Rolled <= 1000000:
            if Rolled_2 == 1:
            	Item = "La ostia (Epico)"
            else:
                Item = "Epico"
        elif Rolled <= 3000000:
            if Rolled_2 <= 9:
            	Item = "Raro"
            else:
            	Item = "Silly (Raro)"
        elif Rolled <= 10000000:
            if Rolled_2 == 1 and not check_items(items, "MCRFT (command)"):
            	Item = "MCRFT (command)"
            else:
            	Item = "Normal"
            
        Rolling = False
        if Rolled <= 100000:
        	print(f"¡¡¡Obtuviste '{Item}'!!!")
        	print(Rolled)
        else:
        	print(f"El item es '{Item}'")
        	print(Rolled)

        while True:
            decision = input("¿Quieres guardar el ítem? [Y/N]: ").lower()
            if decision == "y":
                items.append(Item)
                save_items(items, 'items.txt')
                print("Item guardado.")
                if check_items(items, "Unfunny"):
                	time.sleep(0.5)
                else:
                	time.sleep(2)
                Menu()
                break
            elif decision == "n":
                print("Item descartado.")
                if check_items(items, "Unfunny"):
                	time.sleep(0.5)
                else:
                	time.sleep(2)
                Menu()
                break
            else:
                print("Respuesta inválida. Por favor, responde con Y o N.")
                
        InMenu = False

def Menu():
    global MC
    global MainG
    
    MC = False
    MainG = True
    
    global InMenu
    if not InMenu:
        InMenu = True
        
    Clear()
    print("Comandos:")
    print("")
    print("R - Consigues un item de una calidad aleatoria")
    print("L - Muestra tu inventario")
    print("Z - Elimina un item de tu inventario")
    print("Q - Salir")
    print("C - Craftear")
    if check_items(items, "Medalla"):
    	print("U - Usar item")
    print("")
    Respuesta = input(">>> ").lower()
    
    if Respuesta == "r":
        Roll()
    elif Respuesta == "l":
        print("")
        print_items(items)
        print("")
        input("Presiona Enter para continuar...")
        Clear()
        Menu()
    elif Respuesta == "z":
    	remove_items(items)
    elif Respuesta == "q":
    	Clear()
    	print("Saliendo...")
    	time.sleep(2)
    elif Respuesta == "c":
    	print("Crafteos:")
    	print("")
    	print("[1] Equilibrio - Ying + Yang")
    	print("[2] Pou celestial - Pou + Godly")
    	print("[3] Unfunny - Silly + Normal x10 <- (Da un x4 a la velocidad de                                                   manejo de items)")
    	print("[4] Mega epico - Epico x20 + legendario")
    	print("")
    	Crafting = input(str(">>> ")).lower()
    	if Crafting == "1":
    		Craft(items, "Ying", 1, "Yang", 1, "Equilibrio")
    	elif Crafting == "2":
    		Craft(items, "Pou (Legendario)", 1, "Godly (Mitico)", 1, "Pou celestial")
    	elif Crafting == "3":
    		Craft(items, "Silly (Raro)", 1, "Normal", 10, "Unfunny")
    	elif Crafting == "4":
    		Craft(items, "Epico", 20, "Legendario", 1, "Mega epico")
    elif Respuesta == "mcrft" and check_items(items, "MCRFT (command)"):
    	MCRFT()
    elif Respuesta == "u" and check_items(items, "Medalla"):
	    print("[1] Dragon gem")
	    print("[2] OP")
	    Using = input(str(">>> "))
    if Using == "1" and check_items(items, "Dragon gem"):
    	Item = "~Dragonborn~"
    	items.append(Item)
    	save_items(items, 'items.txt')
    	Del_i(items, "Dragon gem")
    	print(f"Ahora eres un {Item}...")
    	time.sleep(2)
    	Menu()
    elif Using == "2" and check_items(items, "OP"):
    	print("...")
    	time.sleep(2)
    	Item = "~Admin~"
    	items.append(Item)
    	save_items(items, 'items.txt')
    	Del_i(items, "OP")
    	print(f"Ahora eres un {Item}...")
    	time.sleep(2)
    	Menu()
    	
    else:
        print("Respuesta invalida")
        time.sleep(1)
        Clear()
        Menu()

if not InMenu:
    items = load_items('items.txt')
    Menu()