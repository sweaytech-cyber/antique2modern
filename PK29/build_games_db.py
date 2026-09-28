import os
import re
import json

directory = r"c:\Users\nasar\Downloads\AERO 92\PK 29"

TITLE_OVERRIDES = {
    "1v1lol.html": "1v1.LOL",
    "2048.html": "2048 Game",
    "8ballpool.html": "8 Ball Pool",
    "adarkroom.html": "A Dark Room",
    "adatewithdeath.html": "A Date with Death",
    "adayintheoffice.html": "A Day in the Office",
    "adventneon.html": "Advent Neon",
    "adventurecapitalist.html": "Adventure Capitalist",
    "agariolite.html": "Agar.io Lite",
    "airlinetycoonidle.html": "Airline Tycoon Idle",
    "alienskyinvasion.html": "Alien Sky Invasion",
    "amongus.html": "Among Us",
    "angrybirds.html": "Angry Birds",
    "angrybirdsshowdown.html": "Angry Birds Showdown",
    "antimatterdimensions.html": "Antimatter Dimensions",
    "aquaparkio.html": "Aquapark.io",
    "archeryworldtour.html": "Archery World Tour",
    "asmallworldcup.html": "A Small World Cup",
    "backrooms.html": "The Backrooms 3D",
    "backrooms2d.html": "Backrooms 2D",
    "badparenting.html": "Bad Parenting",
    "badtimesim.html": "Sans Boss Fight (Bad Time Sim)",
    "baldisbasics.html": "Baldi's Basics Classic",
    "baldisbasicsremaster.html": "Baldi's Basics Remastered",
    "ballblast.html": "Ball Blast",
    "baseballbros.html": "Baseball Bros",
    "basketballlegends.html": "Basketball Legends",
    "basketballstars.html": "Basketball Stars",
    "basketbros.html": "Basket Bros",
    "basketrandom.html": "Basket Random",
    "bitlife.html": "BitLife Simulator",
    "blockblast.html": "Block Blast!",
    "blockpost.html": "Blockpost 3D",
    "bloonstd6scratch.html": "Bloons TD 6",
    "bobtherobber2.html": "Bob The Robber 2",
    "bobtherobber5.html": "Bob The Robber 5",
    "brawlstars.html": "Brawl Stars",
    "buildnowgg.html": "BuildNow GG",
    "burritobisonlaunchalibre.html": "Burrito Bison: Launcha Libre",
    "capybaraicker.html": "Capybara Clicker",
    "catmario.html": "Cat Mario (Syobon Action)",
    "celeste.html": "Celeste Classic",
    "celeste2.html": "Celeste 2",
    "chatbot.html": "AI Chatbot",
    "choppyorc.html": "Choppy Orc",
    "cookieclicker.html": "Cookie Clicker",
    "crossyroad.html": "Crossy Road",
    "cs16.html": "Counter-Strike 1.6 Web",
    "csgoicker.html": "CS:GO Case Clicker",
    "cuttherope.html": "Cut The Rope",
    "dandysworldicker.html": "Dandy's World Clicker",
    "deadestate.html": "Dead Estate",
    "deadplate.html": "Dead Plate",
    "deltarune.html": "Deltarune Chapter 1",
    "deltatraveler.html": "Deltatraveler",
    "dogeminer.html": "Doge Miner",
    "dogeminer2.html": "Doge Miner 2: Back to the Moon",
    "dokidokiliteratureub.html": "Doki Doki Literature Club",
    "doomemscripten.html": "DOOM (1993)",
    "doomzio.html": "DoomZ.io",
    "dreadheadparkour.html": "Dreadhead Parkour",
    "driftboss.html": "Drift Boss",
    "drifthunters.html": "Drift Hunters",
    "drivemad.html": "Drive Mad",
    "dukenukem3d.html": "Duke Nukem 3D",
    "eaglercraft112.html": "Minecraft 1.12 (Eaglercraft)",
    "eaglercraft152.html": "Minecraft 1.5.2 (Eaglercraft)",
    "eaglercraftalpha126offline.html": "Minecraft Alpha 1.2.6",
    "eaglercraftbeta13offline.html": "Minecraft Beta 1.3",
    "eaglercraftbeta173offline.html": "Minecraft Beta 1.7.3",
    "eaglercraftx188u29.html": "Minecraft 1.8.8 (EaglercraftX)",
    "eggycar.html": "Eggy Car",
    "escaperoad.html": "Escape Road",
    "escaperoad2.html": "Escape Road 2",
    "escaperoadcity.html": "Escape Road City",
    "fallguys.html": "Fall Guys",
    "fearstofathomhomealone.html": "Fears to Fathom: Home Alone",
    "fireboyandwatergirl2.html": "Fireboy & Watergirl 2",
    "fnac1.html": "Five Nights at Candy's 1",
    "fnac2.html": "Five Nights at Candy's 2",
    "fnaf.html": "Five Nights at Freddy's 1",
    "fnaf2.html": "Five Nights at Freddy's 2",
    "fnaf3.html": "Five Nights at Freddy's 3",
    "fnaf4.html": "Five Nights at Freddy's 4",
    "fnafps.html": "FNaF: Pizzeria Simulator",
    "fnafsl.html": "FNaF: Sister Location",
    "fnafucn.html": "FNaF: Ultimate Custom Night",
    "fnafworldd.html": "FNaF World",
    "IDE.html": "Code & Game IDE",
}

FEATURED_GAMES = {
    "1v1lol.html", "eaglercraftx188u29.html", "eaglercraft112.html", "fnaf.html",
    "fnaf2.html", "drifthunters.html", "crossyroad.html", "fallguys.html",
    "cookieclicker.html", "bitlife.html", "basketballstars.html", "basketbros.html",
    "amongus.html", "2048.html", "cs16.html", "cuttherope.html", "doomemscripten.html",
    "drivemad.html", "escaperoad.html", "baldisbasics.html", "catmario.html",
    "celeste.html", "angrybirds.html", "8ballpool.html", "brawlstars.html"
}

CATEGORIES = {
    "Action": ["1v1", "cs", "doom", "brawl", "buildnow", "shooter", "battle", "sniper", "fight", "war", "blood", "duke", "assassin", "bullet", "combat", "strike", "chaos", "derby"],
    "Racing": ["drift", "drive", "car", "racing", "bike", "motorcycle", "vehicle", "escape", "road", "speed", "buggy", "truck", "kart", "runner"],
    "Sports": ["pool", "ball", "basketball", "basket", "baseball", "soccer", "cup", "golf", "archery", "tennis", "bowling", "dunk", "slam", "boxing"],
    "Horror": ["fnaf", "fnac", "fnaw", "backrooms", "fear", "dread", "evil", "ghost", "dead", "plate", "nightmare", "parenting", "baldi"],
    "Sandbox": ["eaglercraft", "craft", "doblox", "doblx", "mine", "block", "build", "sandbox"],
    "Puzzle & Idle": ["2048", "clicker", "icker", "idle", "tycoon", "puzzle", "rope", "dimensions", "cell", "chess", "logic", "dungeon", "deck", "card"],
    "Platformer": ["mario", "celeste", "parkour", "blob", "run", "jump", "goober", "orc", "stickman", "guy"],
}

GRADIENTS = [
    "linear-gradient(135deg, #FF6B6B 0%, #556270 100%)",
    "linear-gradient(135deg, #7F00FF 0%, #E100FF 100%)",
    "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
    "linear-gradient(135deg, #FF4E50 0%, #F9D423 100%)",
    "linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)",
    "linear-gradient(135deg, #f857a6 0%, #ff5858 100%)",
    "linear-gradient(135deg, #4776E6 0%, #8E54E9 100%)",
    "linear-gradient(135deg, #614385 0%, #516395 100%)",
    "linear-gradient(135deg, #e1eec3 0%, #f05053 100%)",
    "linear-gradient(135deg, #02AAB0 0%, #00CDAC 100%)",
    "linear-gradient(135deg, #FF512F 0%, #DD2476 100%)",
    "linear-gradient(135deg, #43C6AC 0%, #F8FFAE 100%)"
]

def clean_name(filename):
    if filename in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[filename]
    
    name = filename.replace(".html", "")
    name = re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', name)
    name = name.replace("_", " ").replace("-", " ")
    
    words = name.split()
    capitalized = []
    for w in words:
        if w.lower() in ["io", "3d", "2d", "gg", "fnf", "cs", "gt"]:
            capitalized.append(w.upper())
        else:
            capitalized.append(w.capitalize())
    return " ".join(capitalized)

def get_category(filename, name):
    fn_lower = filename.lower()
    name_lower = name.lower()
    
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in fn_lower or kw in name_lower:
                return cat
    return "Arcade & Casual"

games = []
for fname in os.listdir(directory):
    if fname.endswith(".html") and fname not in ["index.html", ".html", "fnfshooter.html.crswap"]:
        if fname.startswith("."):
            continue
        filepath = os.path.join(directory, fname)
        if os.path.getsize(filepath) == 0:
            continue
        
        cname = clean_name(fname)
        cat = get_category(fname, cname)
        
        # Consistent color gradient hashing
        grad_idx = sum(ord(c) for c in fname) % len(GRADIENTS)
        
        games.append({
            "id": fname.replace(".html", ""),
            "file": fname,
            "name": cname,
            "category": cat,
            "featured": fname in FEATURED_GAMES,
            "bgGradient": GRADIENTS[grad_idx]
        })

games.sort(key=lambda x: x["name"].lower())

print(f"Total games parsed: {len(games)}")

with open(os.path.join(directory, "games.json"), "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2)

print("Saved clean games.json successfully.")
