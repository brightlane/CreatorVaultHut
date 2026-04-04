import json

affiliate = "https://convert.ctypy.com/aff_c?offer_id=29197&aff_id=21885"

daily_tips = [
    "Stay hydrated throughout the day!",
    "Include protein in every meal.",
    "Track your meals to stay consistent.",
    "Add vegetables to every meal.",
    "Start your day with a healthy breakfast."
]

images = [
    "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=800",
    "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800",
    "https://images.unsplash.com/photo-1506089676908-3592f7389d4d?w=800",
    "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800",
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800"
]

posts = []

for i in range(1, 1001):
    post = {
        "title": f"Nutrisystem Tip #{i}",
        "tip": daily_tips[i % len(daily_tips)],
        "image": images[i % len(images)],
        "link": affiliate
    }
    posts.append(post)

with open("posts.json", "w") as f:
    json.dump(posts, f, indent=2)

print("✅ posts.json with 1000 entries created")
