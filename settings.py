from database import get_db_screen

milestones = [1,5,10,15,20,25,50,100,150,200,250,300,350,400,450]
BambooNames = {
    1: "Micro Sprout",
    5: "Little Shoot",
    10: "Good Plant",
    15: "Strong Stalk",
    20: "Thick Boy",
    25: "Big Guy",
    50: "Earth Piercer",
    100: "The Absolute",
    150: "Forest Giant",
    200: "Legendary Bamboo",
    250: "Hero Bamboo",
    300: "Farmer's Pride",
    350: "Weed Destroyer",
    400: "Explosive Grower",
    450: "Glory to Bamboo"
}

Achivements = {
    1: """0 cm → Micro Sprout
Your bamboo grew... or maybe not 😂
Now you are a Micro Sprout.
Even a microscope won't help here, bro...""",

    5: """5 cm → Little Shoot
Your bamboo grew to 5 cm!
Now you are a Little Shoot.
"Mom, I am not small anymore!" — it said and cried.""",

    10: """10 cm → Good Plant
Your bamboo grew to 10 cm!
Now you are a Good Plant.
Middle class, bro. You can show it to people without shame.""",

    15: """15 cm → Strong Stalk
Your bamboo grew to 15 cm!
Now you are a Strong Stalk.
People respect you now. Others stop laughing and start being afraid.""",

    20: """20 cm → Thick Boy
Your bamboo grew to 20 cm!
Now you are a Thick Boy.
The boss is here. Neighbors look at it with respect 👀""",

    25: """25 cm → Big Guy
Your bamboo grew to 25 cm!
Now you are a Big Guy.
This is serious now. "Mom, look, I am huge!\"""",

    50: """50 cm → Earth Piercer
Your bamboo grew to 50 cm!
Now you are an Earth Piercer.
Wow, this is not just gardening, this is deep drilling 🔥""",

    100: """100 cm → The Absolute
Your bamboo grew to 100 cm!
Now you are The Absolute.
A god came down to earth. Everyone in chat is just silent "....\"""",

    150: """150 cm → Forest Giant
Your bamboo grew to 150 cm!
Now you are a Forest Giant.
I am shocked, bro. This is not a plant, this is a force of nature.""",

    200: """200 cm → Legendary Bamboo
Your bamboo grew to 200 cm!
Now you are the Legendary Bamboo.
It is the end of the world. You are officially the new boss of this chat.
We bow to you 🚩""",

    250: """250 cm → Hero Bamboo
Your bamboo grew to 250 cm!
Now you are the Hero Bamboo.
Not just a plant anymore — it has an idea. Glory to Bamboo! Glory to the heroes (of your bamboo).""",

    300: """300 cm → Farmer's Pride
Your bamboo grew to 300 cm!
Now you are the Farmer's Pride.
While city people measure with rulers, you already planted a field. Real village power. Respect from all the farmers.""",

    350: """350 cm → Weed Destroyer
Your bamboo grew to 350 cm!
Now you are the Weed Destroyer.
Started from a sprout — finished with destroying all weeds. Now you control all the gardens.""",

    400: """400 cm → Explosive Grower
Your bamboo grew to 400 cm!
Now you are the Explosive Grower.
Boom! Everyone is shocked, neighbors ask "what is this crazy thing?". Other plants are scared.""",

    450: """450 cm → Glory to Bamboo
Your bamboo grew to 450 cm!
Now you are "Glory to Bamboo".
That's it. It's not just a size — it's a grand victory. The chat is screaming your name.
Glory to Bamboo! Glory to the heroes 🚩"""


}

def GetTypeBamboo(old_amount,new_amount):
    typeB = "Микрокорнишон"
    message = None;
    for i in milestones:
        if old_amount < i <= new_amount:
            message = Achivements[i]
            break
            
    for i in range(len(milestones)):
        if new_amount >= milestones[i]:
            typeB = BambooNames[milestones[i]]
    return typeB, message
