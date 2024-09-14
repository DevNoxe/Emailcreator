import random
import colorama 
import os
import datetime

# Inicializar colorama para que funcione en todos los sistemas
colorama.init(autoreset=True)

names_boys = [
    "Aaron", "Adam", "Adrian", "Aidan", "Alan", "Albert", "Alexander", "Alfred", "Andrew", 
    "Anthony", "Arthur", "Ashton", "Austin", "Benjamin", "Blake", "Bradley", "Brandon", 
    "Brian", "Bruce", "Caleb", "Cameron", "Carl", "Charles", "Christian", "Christopher", 
    "Clark", "Colin", "Connor", "Craig", "Daniel", "David", "Dean", "Derek", "Dominic", 
    "Dylan", "Edward", "Elijah", "Elliott", "Eric", "Ethan", "Evan", "Felix", "Finn", 
    "Francis", "Frank", "Frederick", "Gabriel", "Gavin", "George", "Gordon", "Grant", 
    "Gregory", "Harry", "Harvey", "Henry", "Hugh", "Ian", "Isaac", "Jack", "Jackson", 
    "Jacob", "James", "Jason", "Jeffrey", "Jeremy", "John", "Jonathan", "Jordan", "Joseph", 
    "Joshua", "Julian", "Keith", "Kevin", "Kyle", "Lance", "Lawrence", "Leo", "Leonard", 
    "Liam", "Louis", "Lucas", "Luke", "Malcolm", "Marcus", "Mark", "Martin", "Matthew", 
    "Max", "Michael", "Miles", "Nathan", "Nicholas", "Noah", "Oliver", "Oscar", "Owen", 
    "Patrick", "Paul", "Peter", "Philip", "Raymond", "Richard", "Robert", "Robin", "Roger", 
    "Ryan", "Samuel", "Scott", "Sean", "Sebastian", "Simon", "Stephen", "Steven", "Theodore", 
    "Thomas", "Timothy", "Toby", "Tristan", "Victor", "Vincent", "Walter", "William", "Zachary",
    "Adrien", "Alain", "Alexandre", "Alphonse", "Antoine", "Armand", "Arthur", "Augustin", 
    "Bastien", "Benoît", "Bernard", "Bruno", "Cédric", "Charles", "Christophe", "Claude", 
    "Clément", "Damien", "Daniel", "David", "Denis", "Didier", "Dominique", "Édouard", 
    "Émile", "Étienne", "Félix", "Florian", "François", "Frédéric", "Gabriel", "Gaspard", 
    "Georges", "Gérard", "Gilles", "Grégoire", "Guillaume", "Henri", "Hervé", "Hugo", 
    "Jacques", "Jean", "Jérôme", "Joseph", "Jules", "Julien", "Laurent", "Louis", "Luc", 
    "Lucas", "Ludovic", "Marc", "Marcel", "Mathieu", "Maurice", "Maxime", "Michel", 
    "Nicolas", "Olivier", "Pascal", "Patrick", "Paul", "Philippe", "Pierre", "Quentin", 
    "Raphaël", "Raymond", "Rémy", "René", "Romain", "Sébastien", "Simon", "Stéphane", 
    "Théodore", "Théo", "Thierry", "Thomas", "Tristan", "Victor", "Vincent", "Xavier", 
    "Yannick", "Yves", "Zacharie",
    "Adrián", "Agustín", "Alejandro", "Alfonso", "Álvaro", "Andrés", "Antonio", "Armando", 
    "Arturo", "Benjamín", "Bruno", "Camilo", "Carlos", "César", "Cristian", "Cristóbal", 
    "Daniel", "David", "Diego", "Domingo", "Eduardo", "Emilio", "Enrique", "Esteban", 
    "Felipe", "Fernando", "Francisco", "Gabriel", "Gonzalo", "Guillermo", "Héctor", 
    "Hugo", "Ignacio", "Isaac", "Ismael", "Iván", "Jaime", "Javier", "Jesús", "Joaquín", 
    "Jorge", "José", "Juan", "Julio", "Leandro", "Leonardo", "Lorenzo", "Lucas", "Luis", 
    "Manuel", "Marcos", "Mario", "Martín", "Mateo", "Miguel", "Nicolás", "Óscar", "Pablo", 
    "Pedro", "Rafael", "Ramón", "Raúl", "Ricardo", "Roberto", "Rodrigo", "Rubén", "Salvador", 
    "Samuel", "Santiago", "Sergio", "Tomás", "Vicente", "Víctor", "Xavier", "Zacarías"
]

names_girls = [
    "Abigail", "Alice", "Amanda", "Amelia", "Amy", "Angela", "Anna", "Anne", "Audrey", 
    "Ava", "Barbara", "Beatrice", "Beth", "Brianna", "Bridget", "Caitlyn", "Carla", "Caroline", 
    "Catherine", "Charlotte", "Chloe", "Claire", "Daisy", "Diana", "Donna", "Dorothy", 
    "Eleanor", "Elizabeth", "Ella", "Ellen", "Emily", "Emma", "Erin", "Eva", "Evelyn", 
    "Fiona", "Florence", "Frances", "Gabrielle", "Georgia", "Grace", "Hannah", "Harper", 
    "Hazel", "Heather", "Helen", "Holly", "Isabella", "Isla", "Ivy", "Jane", "Janet", 
    "Jennifer", "Jessica", "Joan", "Jocelyn", "Josephine", "Joyce", "Judith", "Julia", 
    "Katherine", "Katie", "Kayla", "Kimberly", "Lara", "Laura", "Lauren", "Leah", "Lillian", 
    "Lily", "Lucy", "Madeline", "Margaret", "Maria", "Martha", "Mary", "Megan", "Melanie", 
    "Melissa", "Mia", "Michelle", "Molly", "Natalie", "Nina", "Olivia", "Pamela", "Patricia", 
    "Paula", "Penelope", "Rachel", "Rebecca", "Rose", "Ruby", "Samantha", "Sarah", "Scarlett", 
    "Sophia", "Stella", "Stephanie", "Susan", "Sylvia", "Tessa", "Valerie", "Vanessa", 
    "Victoria", "Violet", "Vivian", "Wendy", "Willow", "Zoe",
    "Adèle", "Adrienne", "Agnès", "Alice", "Amélie", "Anaïs", "Anne", "Ariane", "Audrey", 
    "Aurélie", "Aurore", "Bernadette", "Camille", "Catherine", "Cécile", "Chantal", "Charlotte", 
    "Christelle", "Claire", "Clarisse", "Claudine", "Clémence", "Colette", "Coralie", "Corinne", 
    "Danielle", "Delphine", "Denise", "Dominique", "Éliane", "Élisabeth", "Élodie", "Emmanuelle", 
    "Estelle", "Eugénie", "Eva", "Fanny", "Florence", "Françoise", "Gabrielle", "Geneviève", 
    "Hélène", "Isabelle", "Jacqueline", "Jeanne", "Joséphine", "Julie", "Juliette", "Laure", 
    "Léa", "Louise", "Lucie", "Madeleine", "Manon", "Margaux", "Marguerite", "Marie", "Marielle", 
    "Marine", "Marion", "Martine", "Mathilde", "Mélanie", "Michelle", "Monique", "Nathalie", 
    "Nicole", "Noémie", "Odette", "Pauline", "Renée", "Sabine", "Sandrine", "Sophie", "Stéphanie", 
    "Suzanne", "Sylvie", "Thérèse", "Valérie", "Vanessa", "Véronique", "Victoire", "Viviane", 
    "Yvonne", "Zoé",
    "Adriana", "Alejandra", "Alicia", "Ángela", "Antonia", "Ariadna", "Beatriz", "Blanca", 
    "Berta", "Camila", "Carla", "Catalina", "Carmen", "Cecilia", "Claudia", "Cristina", 
    "Daniela", "Diana", "Elena", "Elsa", "Emilia", "Estefanía", "Eugenia", "Evelyn", 
    "Gabriela", "Gloria", "Graciela", "Guadalupe", "Inés", "Irene", "Isabel", "Jazmín", 
    "Jimena", "Johana", "Juana", "Juliana", "Karina", "Laura", "Leidy", "Lina", "Lucía", 
    "María", "Marta", "María José", "Martina", "Melissa", "Mercedes", "Natalia", "Nerea", 
    "Noelia", "Olga", "Paola", "Patricia", "Raquel", "Rocío", "Sandra", "Sara", "Sofía", 
    "Tamara", "Teresa", "Valeria", "Vanessa", "Verónica", "Victoria", "Yolanda", "Zoe"
]

surnames = [
    "Álvarez", "Bermúdez", "Blanco", "Cabrera", "Castillo", "Castro", "Chávez", "Díaz", 
    "Domínguez", "Fernández", "Flores", "García", "Gómez", "González", "Gutiérrez", 
    "Hernández", "Jiménez", "López", "Martínez", "Mendoza", "Morales", "Muñoz", 
    "Navarro", "Orozco", "Ortiz", "Pérez", "Ramírez", "Ramos", "Reyes", "Rivera", 
    "Rodríguez", "Romero", "Ruiz", "Salazar", "Sánchez", "Serrano", "Torres", 
    "Vargas", "Vázquez", "Vega", "Zamora", "Aguirre", "Arias", "Araya", "Araya", 
    "Bermúdez", "Bravo", "Bravo", "Bustos", "Cardenas", "Carrillo", "Cifuentes", "Cuellar", 
    "Díaz", "Flores", "Gallego", "García", "Gómez", "González", "Gutiérrez", "Jara", 
    "Jaramillo", "López", "Martínez", "Morales", "Muñoz", "Paredes", "Pérez", "Ramírez", 
    "Ríos", "Robles", "Rojas", "Ruiz", "Sánchez", "Serrano", "Silva", "Vega", "Vera"
]

def choose_name():
    global sex, b, a
    sex = input("You are a boy or a girl? -> boy/girl: ").strip().lower()

    while sex not in ["boy", "girl"]:
        print("You have to choose 'boy' or 'girl'.")
        os.system("cls")  # Usar 'cls' para Windows, en Linux/Mac se usa 'clear'
        sex = input("You are a boy or a girl? -> boy/girl: ").strip().lower()

    if sex == "boy":
        b = random.choice(names_boys)
    elif sex == "girl":
        a = random.choice(names_girls)

choose_name()

def choose_surnames():
    global d
    d = random.choice(surnames)

choose_surnames()

def generar_fecha_nacimiento():
    # Generar año aleatorio entre 1950 y 2005
    year = random.randint(1950, 2005)
    
    # Generar mes aleatorio entre 1 y 12
    month = random.randint(1, 12)
    
    # Determinar el número máximo de días en el mes
    last_day_of_month = (datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)).day if month < 12 else 31
    
    # Generar día aleatorio válido para el mes
    day = random.randint(1, last_day_of_month)
    
    return f"{day:02d}/{month:02d}/{year}"

fecha_nacimiento = generar_fecha_nacimiento()

def generar_email():
    global email
    if sex == "boy":
        name_part = b.lower()
    elif sex == "girl":
        name_part = a.lower()
    
    number = random.randint(1, 99)  # Número aleatorio entre 1 y 99
    separator = random.choice(['.', '_', '-'])
    email_formats = [
        f"{name_part}{separator}{d.lower()}@example.com",
        f"{name_part}{separator}{number}@example.com",
        f"{name_part}{number}{separator}{d.lower()}@example.com",
        f"{name_part}{separator}{number}{separator}{d.lower()}@example.com",
        f"{name_part}{separator}{d.lower()}{number}@example.com",
        f"{name_part}{separator}{d.lower()}@example.com",
    ]
    
    email = random.choice(email_formats)

generar_email()

print(f"Nombre: {b if sex == 'boy' else a} {d}")
print(f"Fecha de nacimiento: {fecha_nacimiento}")
print(f"Email sugerido: {email}")

print("You can take a temporary number phone at https://sms-man.com/es/free-numbers")