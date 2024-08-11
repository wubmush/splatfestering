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

# List of potential themes for two-way Splatfests
themes_two_way = [
    "Rice vs Bread", "Red Kitsune Udon vs Green Tanuki Soba", "Lemon Tea vs Milk Tea", "Grasshopper vs Ant", "Airhead vs Wisecracker", "Squid vs Octopus (as food)", "Love vs Money", "Land Food vs Seafood",
    "Perfect Body vs Perfect Mind", "Pokémon Red vs Pokémon Green", "Show No Mercy! vs Focus on Healing", "Tuna & Mayonaisse vs Red Salmon", "Black Tie Event vs Fancy Dress Party", "Chocorooms vs Chococones",
    "Callie vs Marie", "Cats vs Dogs", "Roller Coasters vs Water Slides", "Marshmallows vs Hot Dogs", "Autobots vs Decepticons", "Art vs Science", "Cars vs Planes", "Pirates vs Ninjas", "Burgers vs Pizza",
    "Naughty vs Nice", "Past vs Future", "Pokémon Red vs Pokémon Blue", "Snowman vs Sandcastle", "SpongeBob vs Patrick", "Early Bird vs Night Owl", "Rock vs Pop", "Eating vs Sleeping",
    "North Pole vs South Pole", "Messy vs Tidy", "Zombies vs Ghosts", "Pineapple on Pizza is Delicious vs Pineapple on Pizza is Disgusting", "Get Fit vs Get Rich", "Play Like a Barbarian vs Play Like a Ninja",
    "Hoverboard vs Jet Pack", "World Tour vs Space Adventure", "Mayo vs Ketchup", "Fries vs McNuggets", "Dexterity vs Tenacity", "Drinks With Lemon vs Drinks Without Lemon", "Warm Innerwear vs Warm Outerwear",
    "Action vs Comedy", "Emperor vs Goggles", "Flowers vs Dumplings", "Newest Shoes vs Most Popular Shoes", "New Life-Forms vs Advanced Technology", "Hello Kitty vs Cinnamoroll", "My Melody vs Pompompurin",
    "Hello Kitty vs My Melody", "Squid vs Octopus (as characters)", "Tsubuan vs Koshian", "Trick vs Treat", "Pocky Chocolate vs Pocky Gokubosu", "Hero vs Villain", "Family vs Friend", "Airhead vs Wisecracker",
    "Knight vs Wizard", "Hare vs Tortoise", "Ce League vs Pa League", "Subuta Without Pineapple vs Subuta With Pineapple", "Chaos vs Order", "Chicken vs Egg", "Super Mushroom vs Super Star",
    "Cake vs Ice Cream", "Flight vs Invisibility", "Vampire vs Werewolf", "Sci-Fi vs Fantasy", "Christmas Sweater vs Christmas Socks", "Money vs Love", "Baseball vs Football", "Raph vs Leo", "Mikey vs Donnie",
    "Raph vs. Donnie", "Pulp vs No Pulp (in orange juice)", "Fork vs Spoon", "Retro vs Modern", "Salsa vs Guacamole", "Pancakes vs Waffles", "Time Travel vs Teleportation", "Unicorn vs Narwhal",
    "Toilet Paper on the Front of the Roll vs Toilet Paper on the Back of the Roll", "Warm Breakfast vs Cold Breakfast", "Film vs Book", "Gherk-OUT vs Gherk-IN (on burgers)", "Salty vs Sweet",
    "Adventure vs Relax", "Eat It First vs Save It for Last", "Kid vs Grown-Up", 
    "Skiing vs Snowboarding", "Dinosaurs vs Robots", "Alien Invasion vs Zombie Apocalypse", "Sunrise vs Sunset", "Winter vs Summer", 
    "Hot Coffee vs Iced Coffee", "Rain vs Snow", "Ballet vs Hip-Hop", "Pirates vs Knights", "Burger vs Hot Dog", 
    "Cake vs Pie", "Books vs Podcasts", "Pizza vs Tacos", "Football vs Basketball", "Ninja vs Samurai", 
    "Beaches vs Mountains", "Chocolate vs Vanilla", "Cookies vs Brownies", "Dragons vs Unicorns", "Morning vs Night", 
    "Spaghetti vs Lasagna", "Cupcakes vs Donuts", "Dragon vs Phoenix", "Fairy Tales vs Horror", "Coffee vs Tea", 
    "Super Strength vs Super Speed", "Holmes vs Watson", "Smoothies vs Milkshakes", "Magic vs Science", "Burgers vs Sandwiches", 
    "Reliable Excavation Demolition vs Builders League United", "Dinosaurs vs Dragons", "Football vs Baseball", "Electric Guitar vs Acoustic Guitar", 
    "Sun vs Moon", "Ice Cream vs Ice Lollies", "Rainy Day vs Sunny Day", "Aliens vs Robots", "Jedi vs Sith", 
    "Spicy vs Sweet", "Pizza vs Pasta", "Mermaids vs Sea Monsters", "Reading vs Writing", "Sonic vs Knuckles", 
    "Mario vs Luigi", "Movies vs TV Shows", "Jeans vs Sweatpants", "Ice Skating vs Rollerblading", 
    "Tea vs Juice", "Rural vs Urban", "Kirk vs Spock", "Tacos vs Burritos", 
    "Ketchup vs Mustard", "Fruits vs Vegetables", "Rainforest vs Desert", "Mountains vs Valleys", 
    "Muffins vs Cupcakes", "Rei vs Asuka", "Bicycles vs Skateboards", "Hot Chocolate vs Apple Cider", 
    "Comedy Movies vs Horror Movies", "Board Games vs Video Games", "Sandals vs Boots", "Candles vs Incense", 
    "Sunset vs Starry Night", "Rooftop vs Basement", "Hiking vs Swimming", "Camping vs Glamping", 
    "Dogs vs Wolves", "Cakes vs Sweets", "Fireworks vs Bonfires", "Cookies vs Sweets", "Ocean vs Space", 
    "Fast Food vs Home Cooked", "Books vs Comics", "Travel by Plane vs Travel by Train", "Volcanoes vs Tornadoes", 
    "Street Food vs Gourmet Cuisine", "First-Person Shooter vs Third-Person Shooter", "Handheld Consoles vs Home Consoles", 
    "Superman vs Batman", "Meat vs Veg", "Pastel Colors vs Bright Colors", "Lakes vs Oceans", 
    "City Lights vs Starry Nights", "Breakfast vs Dinner", "Freedom vs Safety", "Romeo vs Juliet", "Strawberries vs Grapes", "Ruby vs Sapphire", "Fire vs Water", "Blood vs Tears", "Life vs Death",
    "Greek vs Roman", "Black Clothes vs White Clothes", "Phoenix Wright vs Miles Edgeworth", "Sharks vs Eels", "Rebels vs Empire", "Biology vs Archaeology", "Snowy Owl vs Barn Owl", "Duck vs Goose",
    "Polar Bear vs Grizzly Bear", "Rare vs Well-Done", "Mewtwo vs Mew", "James Bond vs SPECTRE", "Basil vs Rosemary", "To Be vs Not To Be", "Sans vs Papyrus", "Angels vs Demons", "OK Computer vs Kid A",
    "Half-Life vs Portal", "Lennon vs McCartney", "Tom Nook vs Isabelle", "Major Tom vs Ziggy Stardust", "Mario vs Wario", "Wario vs Waluigi", "Peach vs Daisy", "Professor Layton vs Luke Triton",
    "Police vs Fire Department", "Defence Attorney vs Prosecutor", "Hamlet vs Macbeth", "Calamari Inkantation vs Fly Octo Fly", "Monkeys vs Bloons", "Commander Tartar vs Mr. Grizz", "Nausea vs Insomnia",
    "Peeing vs Pooping", "Golf vs Tennis", "King Kong vs Godzilla", "The Batter vs The Judge", "Calvin vs Hobbes", "Tyrannosaurs vs Velociraptors", "Herons vs Cormorants", "Moorhens vs Coots",
    "Pro-Skub vs Anti-Skub", "Skin vs Bone", "Cheese Bagel vs Cinnamon-Raisin Bagel", "Unicorn vs Pegasus", "Sponge vs Coral", "Swords vs Guns", "Space vs Time", "Freddy vs Jason", "Prequel vs Sequel",
    "Left Twix vs Right Twix", "Pull the Lever vs Don't Pull It (trolley problem)", "Proton vs Neutron", "The Doctor vs The Master",
    "Waterfalls vs Geysers", "Cycling vs Jogging", "Hats vs Scarves", "Dinosaurs vs Aliens", "Beethoven vs Mozart", "Sunflowers vs Roses", "Lava Lamp vs Disco Ball", "Lightning vs Thunder",
    "Bishop vs Rook", "Cola vs Lemonade", "Sneakers vs Sandals", "Marathon vs Sprint", "Snowboarding vs Surfing", "Spring vs Autumn", "Wizards vs Alchemists", "Camping Tent vs RV", 
    "Butterflies vs Moths", "Zodiac vs MBTI", "Comedy vs Drama", "Puzzles vs Mazes", "Cat vs Owl", "Breakfast for Dinner vs Dinner for Breakfast", "Rainy Day vs Snowy Day",
    "Butter vs Margarine", "History vs Geography", "Spy vs Detective", "Ice vs Fire", "Painting vs Drawing", "Picnic vs Barbecue", "Morning Coffee vs Afternoon Tea", "Shopping Online vs In-Store Shopping", 
    "Bats vs Owls", "Hot Springs vs Saunas", "Ancient Egypt vs Ancient Greece", "Beach Volleyball vs Indoor Volleyball", "Leather Jacket vs Denim Jacket", "Night Sky vs Clouds", 
    "Chocolate Cake vs Cheesecake", "Ghosts vs Vampires", "History Museum vs Art Gallery", "Jazz vs Blues", "High Fantasy vs Urban Fantasy", "Manga vs Anime", "Soccer Cleats vs Running Shoes",
    "Sweatshirt vs Hoodie", "Aliens vs Mythical Creatures", "Chess vs Go", "Sand vs Snow", "Pandas vs Koalas", "Graffiti vs Murals", "Canoeing vs Kayaking", "Chocolate Chip Cookies vs Sugar Cookies",
    "Mozzarella vs Cheddar", "Popcorn vs Pretzels", "Antique vs Modern", "City Park vs National Park", "Freestyle Swimming vs Backstroke", "Vegetarian vs Vegan", "Soda vs Juice", 
    "Photography vs Painting", "Neon Colors vs Pastel Colors", "Skiing vs Snowboarding", "Sandcastle vs Snowfort", "Pumpkin Pie vs Apple Pie", "Chocolate Milk vs Strawberry Milk", 
    "Sherlock Holmes vs Arsene Lupin", "Mansion vs Penthouse", "Breakfast Tacos vs Breakfast Burritos", "Manga vs Comic Books", "Pterodactyl vs Triceratops", "Supervillain vs Anti-Hero", 
    "Flood vs Drought", "Tea with Sugar vs Tea without Sugar", "Glass Bottle vs Plastic Bottle", "Live Concert vs Music Festival", "Western Movies vs Samurai Movies", "Army vs Navy", 
    "Giant Robots vs Giant Monsters", "Living Room vs Bedroom", "Physics vs Chemistry", "Canoeing vs Rafting", "Renaissance vs Baroque", "Street Racing vs Drag Racing", "Home Gym vs Public Gym", 
    "Dark Chocolate vs Milk Chocolate", "Punk vs Metal", "Wool Sweater vs Cotton Sweater", "Boxing vs Wrestling", "Hot Springs vs Hot Tub", "Ghosts vs Ghostbusters", "Sugar vs Spice", 
    "Chocolates vs Flowers (as gifts)", "Fossils vs Crystals", "Martial Arts vs Yoga", "Man vs Machine", "Poetry vs Prose", "High Heels vs Flats", "Candy Floss vs Ice Cream", "Fencing vs Archery", 
    "Deserts vs Swamps", "Virtual Reality vs Augmented Reality", "UFOs vs Loch Ness Monster", "Samurai vs Ronin", "Mothman vs Bigfoot", "Robots vs Cyborgs", "Lollipops vs Bubble Gum", 
    "Pajamas vs Nightgown", "Wind Power vs Hydroelectric Power", "Firefighter vs Coastguard", "Libraries vs Bookstores", "Hiking Boots vs Running Shoes", "Card Games vs Board Games", 
    "Crossword  vs Sudoku", "Shower vs Bath", "Bubble Bath vs Epsom Salt Bath", "Dance vs Song", "$100,000 Now vs $10,000 Per Year", "City Skyline vs Mountain View", 
    "Documentary vs Mockumentary", "Mythology vs Folklore", "Sour Candy vs Sweet Candy", "Puzzle Games vs Strategy Games", "Nail Polish vs Lipstick", "Skateboarding vs Snowboarding", 
    "Virtual Travel vs Physical Travel", "Candy Corn vs Jelly Beans", "Astronomy vs Astrology", "Swimming Pool vs Beach", "Smartwatch vs Fitness Tracker", "Toffee vs Fudge", 
    "White Chocolate vs Dark Chocolate", "Matcha vs Chai", "Minimalism vs Maximalism", "Piano vs Guitar", "Road Trip vs Cruise", "Magic Tricks vs Juggling", "Boardwalk vs Pier", 
    "Fortune Cookies vs Biscotti", "Puzzle Box vs Puzzle Cube", "Rainforest vs Tundra", "Ski Lodge vs Beach House", "Amusement Park vs Water Park", "Submarine vs Helicopter", 
    "Mazes vs Labyrinths", "Origami vs Paper Mache", "Dragonflies vs Butterflies", "Zebras vs Giraffes", "Sharks vs Dolphins", "Space Opera vs Cyberpunk", "Cooked Sushi vs Raw Sushi", 
    "Plastic Straws vs Paper Straws", "Tropical vs Temperate", "Mystery Novels vs Sci-Fi Novels", "Horror Movies vs Thriller Movies", "Podcast vs Audiobook", "Tigers vs Lions", 
    "Shopping Mall vs Department Store", "Hiking Trail vs Walking Path", "Frozen Yogurt vs Ice Cream", "Fantasy vs Reality", "Outer Space vs Deep Ocean", "Ice Cream Cone vs Ice Cream Cup", 
    "Platformers vs Racing", "Teleportation vs Telekinesis", "Wonderland vs The Looking-Glass (Alice)", "Master Hand vs Crazy Hand", "Hero vs Antihero", "Radio vs Television", 
    "Beachfront vs Lakefront", "Street Art vs Fine Art", "Face Paint vs Masks", "Carnivals vs Circuses", "Jazz Band vs Rock Band", "Stormy Weather vs Clear Weather", "Thunderstorm vs Blizzard", 
    "Karaoke Night vs Movie Night", "Night In vs Night Out", "Steak vs Salmon", "Pizza Oven vs Grill", "Whale Watching vs Safari", "Witch vs Warlock", "Viking vs Samurai", 
    "Solar Eclipse vs Lunar Eclipse", "Red Grapes vs White Wine", "Detective Novels vs Spy Novels", "String Lights vs Lanterns", "Hamster vs Guinea Pig", "Adventure Novel vs Mystery Novel", 
    "Classic Literature vs Modern Fiction", "Anime vs Western Cartoons", "Fruits vs Sweets", "Rock Music vs Hip-Hop", "Beef Burger vs Chicken Burger", "Steak vs Lobster", 
    "Camping under Stars vs Camping in Tent", "Digital Art vs Traditional Art", "Rollerblades vs Ice Skates", "Trilogy vs Quadrilogy", "Breakfast vs Brunch", "Chess vs Checkers", 
    "Black Coffee vs Cream and Sugar", "Sunflowers vs Tulips", "Sweatpants vs Leggings", "Football vs Rugby", "Hot Chocolate vs Coffee", "Silk vs Satin", "Chickens vs Ducks", 
    "Dawn vs Dusk", "Salted Popcorn vs Sweet Popcorn", "Sushi vs Ramen", "Library vs Bookstore", "Whale Watching vs Dolphin Watching", "Giraffes vs Elephants", "Penguins vs Polar Bears", 
    "Robots vs Monsters", "Soda vs Sparkling Water", "Bacon vs Sausage", "Lightning Storm vs Tornado", "Americano vs Cappuccino", "Art Deco vs Art Nouveau", "Whipped Cream vs Ice Cream", 
    "Island Tour vs Surfing", "Puzzles vs Board Games", "Classical Architecture vs Modern Architecture", "Big City vs Small Town", "Sea vs Lake", "Lightning vs Thunder", "Salty Food vs Sweet Food", 
    "Fireplace vs Firepit", "Warm vs Cold", "Almond Milk vs Soy Milk", "Puzzles vs Riddles", "Romance vs Action", "Supernatural vs Sci-Fi", "Baseball Cap vs Beanie", 
    "Iron Man vs Captain America", "Tundra vs Jungle", "Thor vs Loki", "Restaurant vs Takeaway", "Pure Maths vs Applied Maths", "Safari vs Mountain Trek", "Musicals vs Opera", 
    "Graffiti vs Mosaic", "Lemon vs Lime", "Cartoons vs Live-Action", "Sunny Spring vs Rainy Spring", "Mountains vs Oceans", "Autumn vs Spring", "Rockets vs Planes", "Green Tea vs Black Tea", 
    "Cherryade vs Mango Juice", "Zombies vs Aliens", "Fantasy Books vs Sci-Fi Books", "Renaissance Art vs Modern Art", "Windmill vs Watermill", "Morning Coffee vs Evening Tea", 
    "Street Food vs Home Cooking", "Pasta vs Rice", "Big Cats vs Bears", "Muffins vs Cupcakes", "Sports Cars vs Motorcycles", "House Atreides vs House Harkonnen", "Space Exploration vs Ocean Exploration", 
    "Boxing vs MMA", "File Size vs Video Quality", "Cloudy Sky vs Clear Sky", "Paperback vs Hardback", "Classical Music vs Rock Music", "Paragliding vs Skydiving", 
    "Steam Train vs Maglev", "Fiction vs Non-Fiction", "Mac and Cheese vs Pizza", "Pineapple vs Mango", "Fruit Juice vs Smoothies"
]

# List of potential themes for three-way Splatfests
themes_three_way = [
"Rock vs Paper vs Scissors", "Grass vs Fire vs Water", "Gear vs Grub vs Fun",
"Spicy vs Sweet vs Sour", "Dark Chocolate vs Milk White vs White Chocolate", "Nessie vs Aliens vs Bigfoot (which is real?)",
"Power vs Wisdom vs Courage", "Vanilla vs Strawberry vs Mint Chip", "Money vs Fame vs Love",
"Shiver vs Frye vs Big Man", "Zombie vs Skeleton vs Ghost", "Kaiten-yaki vs Oban-yaki vs Imagawa-yaki",
"Friends vs Family vs Solo", "Red Bean Paste vs Custard vs Whipped Cream", "Lightly Salted vs Consommé vs Salted Seaweed (crisps)",
"Baby Chicks vs Li'l Bunnies vs Bear Cubs", "Same Ol' vs Bucket List vs Save the Day (at world's end)", "Palace vs Theme Park vs Beach (holiday home)",
"Bread vs Rice vs Pasta", "Past vs Present vs Future", "Handshake vs Fist Bump vs Hug",
"Friday vs Saturday vs Sunday", "Drums vs Guitar vs Keyboard", "Commander Tartar vs Mr. Grizz vs DJ Octavio",
"Blue vs Yellow vs Red", "Blood vs Sweat vs Tears", "Birth vs Life vs Death",
"Regice vs Regirock vs Registeel", "Amethyst vs Pearl vs Garnet", "Greek vs Egyptian vs Roman",
"Bacon vs Lettuce vs Tomato", "McCoy vs Kirk vs Spock", "Black Clothes vs White Clothes vs Grey Clothes",
"Squidward vs SpongeBob vs Patrick", "Sharks vs Eels vs Rays", "Octarians vs Inklings vs Salmonids",
"Phoenix Wright vs Athena Cykes vs Apollo Justice", "Franziska von Karma vs Miles Edgeworth vs Godot",
"Sonic vs Tails vs Knuckles", "Toilet Paper on the Front of the Roll vs Toilet Paper on the Back of the Roll vs Toilet Paper Roll Stood Up", "Luke Skywalker vs Leia Organa vs Han Solo",
"Animal vs Vegetable vs Mineral", "Asuka vs Shinji vs Rei", "Snowy Owl vs Barn Owl vs Great Horned Owl",
"Duck vs Goose vs Swan", "Polar Bear vs Grizzly Bear vs Black Bear", "Rare vs Medium vs Well-Done",
"Tartar Sauce vs Mayo vs Ketchup", "Articuno vs Zapdos vs Moltres", "Raiders of the Lost Ark vs The Temple of Doom vs The Last Crusade",
"Basil vs Oregano vs Rosemary", "Kris vs Susie vs Ralsei", "Angels vs Demons vs Mortals", "OK Computer vs Kid A vs In Rainbows", "Tom Nook vs Isabelle vs K.K. Slider", "Mario vs Luigi vs Wario",
"Peach vs Daisy vs Rosalina", "Major Tom vs Ziggy Stardust vs The Thin White Duke", "Police vs Ambulance vs Fire Department", "Defence Attorney vs Prosecutor vs Judge", "Nausea vs Insomnia vs Stomach Pain",
"Peeing vs Pooping vs Farting", "Golf vs Tennis vs Volleyball", "Dedan vs Japhet vs Enoch", "Tyrannosaurs vs Velociraptors vs Spinosaurs", "Herons vs Cormorants vs Kingfishers",
"Moorhens vs Coots vs Goldeneyes", "Pro-Skub vs Anti-Skub vs Skub-Neutral", "Kid vs Teen vs Grown-Up", "Skin vs Muscle vs Bone", "Cheese Bagel vs Cinnamon-Raisin Bagel vs Plain Bagel",
"Unicorn vs Pegasus vs Earth Pony", "Sponge vs Coral vs Anemone", "Sayori vs Yuri vs Natsuki", "Prequel vs Sequel vs Spin-Off", "Proton vs Electron vs Neutron",
"Earth vs Mars vs Venus", "Hot Dog vs Hamburger vs Pizza", "Couch vs Recliner vs Bean Bag Chair", "Forest vs Desert vs Jungle", "Chocolate Cake vs Vanilla Cake vs Red Velvet Cake",
"Werewolf vs Vampire vs Zombie", "Dragon vs Phoenix vs Griffin", "Maths vs Science vs History", "Winter vs Spring vs Summer", "Cowboy vs Pirate vs Knight", "Cat vs Dog vs Bird",
"Shower vs Bath vs Jacuzzi", "Apple vs Orange vs Banana", "Ice Cream vs Sorbet vs Gelato", "Comedy vs Drama vs Horror", "Sunrise vs Sunset vs Midnight",
"Pizza vs Tacos vs Burgers", "Rock vs Pop vs Jazz", "Hiking vs Biking vs Swimming", "Manga vs Anime vs Comics", "Tacos vs Burritos vs Quesadillas",
"The Fellowship of the Ring vs The Two Towers vs The Return of the King",
"Soccer vs American Football vs Basketball", "Mountains vs Beach vs City", "Super Strength vs Super Speed vs Telekinesis",
"The Original Series vs The Next Generation vs Deep Space Nine", "Sushi vs Ramen vs Dumplings",
"Morning vs Afternoon vs Night", "Video Games vs Board Games vs Card Games", "Reading vs Writing vs Drawing", "Rainy Day vs Sunny Day vs Snowy Day", "Fruits vs Vegetables vs Grains",
"Piano vs Guitar vs Drums", "Superman vs Batman vs Wonder Woman", "Poseidon vs Zeus vs Hades", "Chocolate vs Vanilla vs Strawberry", "Trot vs Canter vs Gallop",
"Breakfast vs Lunch vs Dinner", "Chess vs Checkers vs Go", "Bravery vs Ambition vs Logic", "Black Mage vs White Mage vs Red Mage", "Running vs Cycling vs Swimming", "Christmas vs Halloween vs Easter",
"Apple Pie vs Pumpkin Pie vs Pecan Pie", "Whale vs Shark vs Dolphin", "Football vs Basketball vs Baseball", "Fish vs Reptiles vs Birds", "Ice Cream vs Cake vs Pie", "Summer vs Winter vs Autumn",
"Chocolate vs Vanilla vs Mint", "City vs Suburbs vs Countryside", "Lions vs Tigers vs Bears", "Painting vs Drawing vs Sculpting", "Sailing vs Flying vs Driving",
"Spaghetti vs Lasagna vs Ravioli", "Flowers vs Trees vs Shrubs", "Cookies vs Brownies vs Muffins", "Sun vs Moon vs Stars", "Pancakes vs Waffles vs French Toast", "American Football vs Soccer vs Rugby",
"Tea vs Coffee vs Hot Chocolate", "Giraffe vs Elephant vs Rhino", "Rubies vs Sapphires vs Padparadscha", "Sugar vs Spice vs Everything Nice", "Rain vs Snow vs Sleet", "Ocean vs Desert vs Mountains",
"Electric Guitar vs Acoustic Guitar vs Bass Guitar", "Rainforest vs Desert vs Tundra", "Salt vs Pepper vs Garlic", "Puppy vs Kitten vs Bunny", "Ice Cream Cone vs Cup vs Sandwich",
"Mount Everest vs Grand Canyon vs Great Barrier Reef", "Roswell Aliens vs Hopkinsville Goblins vs Chupacabra", "Books vs Movies vs TV Shows", "Dinosaurs vs Dragons vs Robots",
"Crosswords vs Sudoku vs Wordsearches",
"Sunflowers vs Roses vs Daisies", "Frogs vs Toads vs Salamanders", "Beach vs Pool vs Lake", "Sun vs Rain vs Wind", "Jeans vs Shorts vs Skirts", "Muffins vs Donuts vs Cupcakes",
"Camping vs Glamping vs Staying Home", "Cooking vs Baking vs Grilling", "Ballet vs Hip-Hop vs Jazz", "Dogs vs Wolves vs Foxes", "Cookies vs Candy vs Cake", "Waterfall vs Glacier vs Volcano",
"Polar Bears vs Penguins vs Seals", "Ninjas vs Pirates vs Knights", "Mars vs Jupiter vs Saturn", "Coffee vs Tea vs Soda", "Orchestra vs Choir vs Band", "Aliens vs Robots vs Superheroes",
"Cookies vs Brownies vs Ice Cream", "Cycling vs Running vs Swimming", "Books vs Audiobooks vs Podcasts", "Space vs Ocean vs Sky", "Rock vs Pop vs Rap" 
]

# Function to generate a random two-way Splatfest
def generate_two_way_splatfest():
    idols = random.choice(idols_two_way)
    theme = random.choice(themes_two_way)
    return f"Splatfest: {idols[0]} vs {idols[1]} - Theme: {theme}"

# Function to generate a random three-way Splatfest
def generate_three_way_splatfest():
    idols = random.choice(idols_three_way)
    theme = random.choice(themes_three_way)
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
        try:
            user_input = input(prompt).strip()
            if user_input.startswith('0') and len(user_input) > 1:
                raise ValueError("Invalid input: Leading zeros are not allowed.")
            return int(user_input)
        except ValueError as e:
            print(e)

# Main function to run the script
if __name__ == "__main__":
    # Ask user for the number of Splatfests they want to generate
    count = get_valid_input("It is I, John Splatoon. Let me cook up some new Splatfests for you. Woomy. How many do ya want? ")
    
    # Generate the requested number of Splatfests
    generated_splatfests = generate_splatfests(count)
    
    # Print each generated Splatfest
    for splatfest in generated_splatfests:
        print(splatfest)
