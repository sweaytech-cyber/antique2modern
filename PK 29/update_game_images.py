import os
import json
import re

directory = r"c:\Users\nasar\Downloads\AERO 92\PK 29"

# Curated high quality gaming cover imagery mapped by keyword / category
CATEGORY_IMAGES = {
    "Racing": [
        "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500&auto=format&fit=crop"
    ],
    "Action": [
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500&auto=format&fit=crop"
    ],
    "Sports": [
        "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=500&auto=format&fit=crop"
    ],
    "Horror": [
        "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=500&auto=format&fit=crop"
    ],
    "Sandbox": [
        "https://images.unsplash.com/photo-1627856013091-fed6e4e30025?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1587573089734-09cb69c0f2b4?w=500&auto=format&fit=crop"
    ],
    "Puzzle & Idle": [
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1529699211952-734e80c4d42b?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=500&auto=format&fit=crop"
    ],
    "Platformer": [
        "https://images.unsplash.com/photo-1551103782-8ab07afd45c1?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500&auto=format&fit=crop"
    ],
    "Arcade & Casual": [
        "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500&auto=format&fit=crop"
    ]
}

SPECIFIC_IMAGES = {
    "1v1lol": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500&auto=format&fit=crop",
    "2048": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500&auto=format&fit=crop",
    "8ballpool": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=500&auto=format&fit=crop",
    "amongus": "https://images.unsplash.com/photo-1614680376593-902f749f7b6b?w=500&auto=format&fit=crop",
    "angrybirds": "https://images.unsplash.com/photo-1551103782-8ab07afd45c1?w=500&auto=format&fit=crop",
    "baldisbasics": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop",
    "basketballstars": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=500&auto=format&fit=crop",
    "bitlife": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500&auto=format&fit=crop",
    "crossyroad": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500&auto=format&fit=crop",
    "cs16": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop",
    "drifthunters": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&auto=format&fit=crop",
    "drivemad": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&auto=format&fit=crop",
    "eaglercraft112": "https://images.unsplash.com/photo-1627856013091-fed6e4e30025?w=500&auto=format&fit=crop",
    "eaglercraftx188u29": "https://images.unsplash.com/photo-1627856013091-fed6e4e30025?w=500&auto=format&fit=crop",
    "fallguys": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500&auto=format&fit=crop",
    "fnaf": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop"
}

with open(os.path.join(directory, "games.json"), "r", encoding="utf-8") as f:
    games = json.load(f)

for i, g in enumerate(games):
    gid = g["id"]
    cat = g.get("category", "Arcade & Casual")
    
    if gid in SPECIFIC_IMAGES:
        g["image"] = SPECIFIC_IMAGES[gid]
    else:
        imgs = CATEGORY_IMAGES.get(cat, CATEGORY_IMAGES["Arcade & Casual"])
        g["image"] = imgs[i % len(imgs)]

with open(os.path.join(directory, "games.json"), "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2)

print("Updated games.json with picture URLs for every single game!")
