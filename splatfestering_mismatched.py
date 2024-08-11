import random

# Define idols and their groupings
idols_two_way = [
    ("Callie", "Marie"), ("Callie", "Marie"),
    ("Pearl", "Marina"), ("Pearl", "Marina"),
    ("Shiver", "Frye")
]

# Adjusted probability for three-way groups
idols_three_way = [
    ("Shiver", "Frye", "Big Man")
] * 9 + [
    ("Callie", "Marie", "Octavio"),
    ("Pearl", "Marina", "Acht")
] * 3 + [
    ("Squid Sisters", "Off the Hook", "Deep Cut")
]

# Lists of individual words to create random themes
words_list = [
"Rice", "Bread", "Udon", "Soba", "Tea", "Milk", "Grasshopper", "Ant", "Love", "Money", "Food",
"Seafood", "Body", "Mind", "Pokemon", "Red", "Green", "Show", "Healing", "Tuna", "Mayonnaise",
"Salmon", "Event", "Party", "Choco", "Cats", "Dogs", "Coasters", "Slides", "Marshmallows",
"Hot Dogs", "Autobots", "Decepticons", "Art", "Science", "Cars", "Planes", "Pirates", "Ninjas",
"Burgers", "Pizza", "Naughty", "Nice", "Past", "Future", "Snowman", "Sandcastle", "SpongeBob",
"Patrick", "Bird", "Owl", "Muffin", "Cupcake", "Dragon", "Unicorn", "Mermaid", "Monster",
"Reading", "Writing", "Mario", "Luigi", "Jeans", "Sweatpants", "Camping", "Glamping",
"Wolves", "Fireworks", "Bonfires", "Cookies", "Brownies", "Ocean", "Space",
"Fast Food", "Home Cooked", "Books", "Comics", "Plane", "Train", "Volcano", "Tornado",
"Gourmet", "Cuisine", "Consoles", "Shooter", "Meat", "Veg", "Colors", "Lakes", "Mountains",
"Breakfast", "Dinner", "Freedom", "Safety", "Strawberries", "Grapes", "Fire", "Water",
"Blood", "Tears", "Greek", "Roman", "Sharks", "Eels", "Rebels", "Empire", "Snowy",
"Barn", "Duck", "Goose", "Bear", "Tyrannosaurs", "Velociraptors", "Cormorant",
"Moorhen", "Coot", "Pro-Skub", "Anti-Skub", "Cheese", "Cinnamon", "Bagel", "Pegasus",
"Sponge", "Coral", "Swords", "Guns", "Time", "Freddy", "Jason", "Prequel",
"Sequel", "Twix", "Lever", "Proton", "Neutron", "Doctor", "Master", "Waterfall",
"Geyser", "Cycling", "Jogging", "Hats", "Scarves", "Beethoven", "Mozart", "Sunflowers",
"Roses", "Lava", "Lamp", "Disco", "Lightning", "Thunder", "Bishop", "Rook",
"Cola", "Lemonade", "Sneakers", "Sandals", "Marathon", "Sprint", "Snowboarding", "Surfing",
"Spring", "Autumn", "Accordion", "Adventure", "Aeroplanes", "Afternoon", "Aging", "Airwaves",
"Alchemy", "Alligators", "Aloe", "Alphabet", "Ambulance", "Amusement", "Ancient", "Animals",
"Antarctica", "Apples", "Arctic", "Artisan", "Astronomy", "Babies", "Balloons", "Barbecues",
"Bats", "Beach", "Beaches", "Beams", "Beanbags", "Beetles", "Bicycles", "Bigfoot",
"Billiards", "Blenders", "Blizzards", "Bookshelves", "Bouquets", "Bubbles", "Buses", "Cacti",
"Candles", "Capacitors", "Carousels", "Caves", "Chickens", "Chocolates", "Clocks", "Clouds",
"Cocoa", "Computers", "Concerts", "Cotton", "Cows", "Cranberries", "Creepers", "Daisies",
"Darts", "Dinosaurs", "Dolls", "Donuts", "Doughnuts", "Ducks", "Eagles", "Electricity",
"Elephants", "Emeralds", "Fountains", "Frogs", "Fruitcakes", "Galaxies", "Games", "Geodes",
"Giraffes", "Glasses", "Globes", "Gloves", "Goldfish", "Grandpa", "Guitars", "Helicopters",
"Honey", "Horses", "Houses", "Icicles", "Insects", "Jellyfish", "Jukeboxes", "Kangaroos",
"Kites", "Koalas", "Lamps", "Lollipops", "Magnets", "Marbles", "Marmalades", "Masks",
"Music", "Nebulas", "Noodles", "Octopuses", "Oranges", "Oysters", "Pajamas", "Parades",
"Parrots", "Peaches", "Penguins", "Perfume", "Pineapples", "Plates", "Puzzles", "Quests",
"Rainbows", "Robots", "Rollerskates", "Rocks", "Rubber", "Sculptures", "Seashells",
"Snowflakes", "Spacecrafts", "Spaghetti", "Sparklers", "Spectacles", "Starfish", "Storms",
"Suitcases", "Tigers", "Toothbrushes", "Trophies", "Turkeys", "Umbrellas", "Valleys", "Vases",
"Vegetables", "Vikings", "Waffles", "Worms", "Xylophones", "Yachts", "Zebras", "Zeppelins",
"Zippers", "Aerobics", "Airships", "Astronauts", "Ballads", "Baseballs", "Basketballs",
"Beakers", "Bison", "Blackberries", "Bridges", "Broccoli", "Bunnies", "Candies", "Carnivals",
"Caveats", "Climbers", "Crafts", "Denim", "Dictionaries", "Dinos", "Dishwashers", "Divers",
"Dolphins", "Feathers", "Fishing", "Flamingos", "Footballs", "Fruits", "Goblins", "Grapefruits",
"Guavas", "Harmony", "Hurricanes", "Jellybeans", "Jokes", "Lemons", "Macaroni", "Melons",
"Microphones", "Mirrors", "Monkeys", "Mosquitoes", "Paintings", "Pillows", "Poppies",
"Prisms", "Rabbits", "Rosebuds", "Sandwiches", "Seaweed", "Socks", "Stones", "Surfboards",
"Swans", "Telephones", "Toys", "Trampolines", "Trees", "Violets", "Volcanoes", "Wrestlers",
"Acorns", "Accordionists", "Aerosol", "Albatross", "Ammunition", "Amplifiers", "Angels",
"Archery", "Astronautics", "Autographs", "Avocados", "Azaleas", "Ballgames", "Ballet",
"Bandanas", "Barometers", "Bicyclists", "Binoculars", "Birdhouses", "Boats", "Bolts", "Boulevard",
"Buckets", "Bushels", "Buzzards", "Cabinets", "Cafes", "Canaries", "Capri", "Carpets",
"Casseroles", "Castles", "Caterpillars", "Cedar", "Chandeliers", "Choreography", "Cinemas",
"Coconut", "Coloring", "Comets", "Confetti", "Cups", "Curtains", "Dandelions", "Decals",
"Discos", "Doghouses", "Donkeys", "Drums", "Dumplings", "Eclairs", "Eclipses", "Eggs",
"Embroidery", "Emojis", "Engines", "Essays", "Eyeglasses", "Ferns", "Festivals", "Fossils",
"Fractals", "Frappes", "Frosting", "Fungi", "Garlic", "Garlands", "Gazelles", "Gingerbread",
"Glaciers", "Gliders", "Golfing", "Gondolas", "Groceries", "Gyms", "Hammocks", "Holiday",
"Horseshoes", "Icebergs", "Impressions", "Iris", "Ivory", "Jukes", "Juices",
"Kaleidoscopes", "Kitesurfing", "Knots", "Kumquats", "Lace", "Labyrinths", "LEGO", "Lemons",
"Lighthouses", "Lunar", "Marshlands", "Meditation", "Mummies", "Musicals", "Nests", "Newspapers",
"Notebooks", "Nuts", "Oases", "Onions", "Origami", "Ornaments", "Paints", "Palms",
"Pansies", "Patterns", "Peacocks", "Peanuts", "Pebbles", "Pies", "Plays", "Plushies", "Pools",
"Posters", "Quilts", "Quotations", "Raincoats", "Raspberry", "Ribbons", "Robins", "Rosemary",
"Sailboats", "Soda", "Sunflowers", "Tacos", "Tangerines", "Teacups", "Teddy", "Thrones",
"Towels", "Treasures", "Twinkling", "Vines", "Vultures", "Washing", "Whistles", "Wildflowers",
"Wings", "Wreaths", "Zinnias", "Zodiac", "Zucchini", "Airplanes", "Antiques", "Appetizers",
"Arrows", "Bags", "Beavers", "Blades", "Booklets", "Bread", "Bubbles", "Candles", "Carvings",
"Chains", "Chairs", "Chests", "Chickpeas", "Clams", "Coconuts", "Coins", "Combs", "Cosmos",
"Crafts", "Drawings", "Drones", "Fabrics", "Flags", "Gauges", "Ginger", "Grandmas", "Jams",
"Jewels", "Kangaroos", "Kitesurfing", "Knives", "Leathers", "Maps", "Nightlights", "Parachutes",
"Parkas", "Photography", "Plumes", "Poems", "Printers", "Puppets", "Quizzes", "Raindrops",
"Rides", "Sandals", "Shampoo", "Shirts", "Shoes", "Shrubs", "Sidewalks", "Speakers",
"Stationery", "Submarines", "Sunsets", "Textiles", "Tiles", "Toothpicks", "Traffic", "Tunnels",
"Valuables", "Washes", "Wheels", "Windows", "Woodpeckers", "Zombies", "Sherlock Holmes",
"James Bond", "Godzilla", "Toilet Paper on the Front of the Roll", "Toilet Paper on the Back of the Roll",
"Pineapple on Pizza", "Kirk", "Spock", "Jedi", "Sith", "Shredders", "Woodchippers", "Crushers",
"Hailstones", "Poop", "Amethyst", "Pearls", "Scouts", "Soldiers", "Pyromaniacs", "Demolition Men",
"Heavy Weapons", "Engineers", "Medics", "Snipers", "Spies", "War", "Famine", "Pestilence", "Death",
"Pee", "Nothing in Particular"
]

# Function to generate a random theme from individual words
def generate_random_theme():
    theme_words = random.sample(words_list, 2)  # Pick 2 unique words
    return " vs ".join(theme_words)

# Function to generate a random theme from individual words
def generate_random_theme3():
    theme_words = random.sample(words_list, 3)  # Pick 3 unique words
    return " vs ".join(theme_words)

# Function to generate a random two-way Splatfest
def generate_two_way_splatfest():
    idols = random.choice(idols_two_way)
    theme = generate_random_theme()
    return f"Splatfest: {idols[0]} vs {idols[1]} - Theme: {theme}"

# Function to generate a random three-way Splatfest
def generate_three_way_splatfest():
    idols = random.choice(idols_three_way)
    theme = generate_random_theme3()
    return f"Splatfest: {idols[0]} vs {idols[1]} vs {idols[2]} - Theme: {theme}"

# Generate a number of random Splatfests
def generate_splatfests(count):
    splatfests = []
    for _ in range(count):
        if random.choice([True, False]):
            splatfests.append(generate_two_way_splatfest())
        else:
            splatfests.append(generate_three_way_splatfest())
    return splatfests

# Function to get a valid integer input from the user
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("Input cannot be empty.")
            continue
        if user_input.startswith('0') and len(user_input) > 1:
            print("Invalid input: Leading zeros are not allowed.")
            continue
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input: Please enter a valid integer.")

# Main function to run the script
if __name__ == "__main__":
    # Ask user for the number of Splatfests they want to generate
    count = get_valid_input("It is I, John Splatoon. Let me cook up some new Splatfests for you. Ngyes. How many do ya want? ")
    
    # Generate the requested number of Splatfests
    generated_splatfests = generate_splatfests(count)
    
    # Print each generated Splatfest
    for splatfest in generated_splatfests:
        print(splatfest)
