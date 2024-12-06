import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 5000

# Updated categories for deeper analysis
categories = [
    "Women Fashion - Sarees", "Women Fashion - Kurtis", "Men Footwear - Casual Shoes",
    "Men Footwear - Formal Shoes", "Home - Kitchen Appliances", "All Mobile & Accessories - Smartphones",
    "All Mobile & Accessories - Smartwatches", "All Mobile & Accessories - Mobile Holders",
    "All Mobile & Accessories - Mobile Cases & Covers", "Kids - Toys", "Beauty & Personal Care - Makeup",
    "Health & Wellness - Supplements", "Home Decor - Furniture", "Sports - Fitness Equipment",
    "Women Accessories - Handbags", "Men Accessories - Watches", "Kids - Baby Clothing",
    "Home - Vacuum Cleaners", "Health & Wellness - Yoga Accessories", "Beauty & Personal Care - Skincare",
    "Home Decor - Lighting", "Sports - Outdoor Gear"
]

# Updated brands list
brands = [
    "Meesho Originals", "TrendyWear", "FootMate", "HomeEase", "MobileGear", "SmartFit",
    "Beautique", "HealthWise", "DecorMania", "ToyLand", "FashionFusion", "SportEdge",
    "ShinyStyle", "ElegantChoice", "BoldTrends", "FreshGlow", "TechZen", "ActiveGear",
    "LuxuryLine", "UrbanChic", "PlayfulKids", "ComfyHome", "WellnessHub", "PowerSport"
]

# Function to generate a random product name based on category
def generate_product_name(category):
    if "Sarees" in category:
        return random.choice(["Silk Saree", "Cotton Saree", "Georgette Saree", "Chiffon Saree"])
    elif "Kurtis" in category:
        return random.choice(["Anarkali Kurti", "A-Line Kurti", "Straight Kurti", "Flared Kurti"])
    elif "Casual Shoes" in category:
        return random.choice(["Sneakers", "Loafers", "Slip-Ons", "Canvas Shoes"])
    elif "Formal Shoes" in category:
        return random.choice(["Oxford Shoes", "Derby Shoes", "Monk Straps", "Brogues"])
    elif "Kitchen Appliances" in category:
        return random.choice(["Mixer Grinder", "Blender", "Electric Kettle", "Microwave Oven"])
    elif "Smartphones" in category:
        return random.choice(["Android Phone", "iOS Phone", "Gaming Smartphone", "Budget Smartphone"])
    elif "Smartwatches" in category:
        return random.choice(["Fitness Tracker", "Luxury Smartwatch", "Budget Smartwatch", "Kids Smartwatch"])
    elif "Mobile Holders" in category:
        return random.choice(["Magnetic Holder", "Car Mount Holder", "Tabletop Holder", "Adjustable Arm Holder"])
    elif "Mobile Cases & Covers" in category:
        return random.choice(["Silicon Cover", "Flip Cover", "Hard Case", "Transparent Case"])
    elif "Toys" in category:
        return random.choice(["Building Blocks", "Action Figures", "Puzzle Toys", "Plush Toys"])
    elif "Makeup" in category:
        return random.choice(["Lipstick", "Eyeliner", "Foundation", "Blush"])
    elif "Supplements" in category:
        return random.choice(["Protein Powder", "Multivitamin", "Omega-3 Capsules", "Calcium Tablets"])
    elif "Furniture" in category:
        return random.choice(["Wooden Table", "Office Chair", "Sofa Set", "Bookshelf"])
    elif "Fitness Equipment" in category:
        return random.choice(["Yoga Mat", "Dumbbells", "Resistance Bands", "Treadmill"])
    elif "Handbags" in category:
        return random.choice(["Leather Handbag", "Tote Bag", "Clutch Bag", "Sling Bag"])
    elif "Watches" in category:
        return random.choice(["Analog Watch", "Digital Watch", "Smartwatch", "Luxury Watch"])
    elif "Baby Clothing" in category:
        return random.choice(["Baby Romper", "Baby T-Shirt", "Baby Pajamas", "Baby Socks"])
    elif "Vacuum Cleaners" in category:
        return random.choice(["Cordless Vacuum", "Robot Vacuum", "Handheld Vacuum", "Canister Vacuum"])
    elif "Yoga Accessories" in category:
        return random.choice(["Yoga Block", "Yoga Strap", "Yoga Bolster", "Meditation Cushion"])
    elif "Skincare" in category:
        return random.choice(["Face Wash", "Moisturizer", "Sunscreen", "Face Serum"])
    elif "Lighting" in category:
        return random.choice(["LED Lamp", "Chandelier", "Table Lamp", "Wall Sconce"])
    elif "Outdoor Gear" in category:
        return random.choice(["Camping Tent", "Hiking Backpack", "Sleeping Bag", "Trekking Poles"])
    else:
        return fake.word()

# Generate data
product_ids = [f"PROD{str(i).zfill(5)}" for i in range(1, num_records + 1)]
product_categories = random.choices(categories, k=num_records)
product_names = [generate_product_name(cat) for cat in product_categories]
product_brands = random.choices(brands, k=num_records)
prices = [round(random.uniform(100, 10000), 2) for _ in range(num_records)]
stock_levels = [random.randint(0, 500) for _ in range(num_records)]

# Create the DataFrame
products_df = pd.DataFrame({
    "product_id": product_ids,
    "product_name": product_names,
    "category": product_categories,
    "brand": product_brands,
    "price": prices,
    "stock": stock_levels
})

# Save the DataFrame to a CSV file
products_df.to_csv("products.csv", index=False)

# Print a sample of the generated data
print(products_df.head())
