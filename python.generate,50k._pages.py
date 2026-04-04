# ULTIMATE VOLUME: generate_500k_pages.py
import pandas as pd
import itertools
import os

# 1. ALL CITIES (30K)
cities_df = pd.read_csv('https://raw.githubusercontent.com/kelvins/US-Cities-Database/main/csv/us_cities.csv', sep=';')

# 2. ZIP multipliers (10x volume)
zip_multipliers = ['main', 'north', 'south', 'east', 'west', 'downtown', 'center']

# 3. Keywords (20x volume)  
keywords = ['tips', 'delivery', 'weight-loss', 'portion-control', 'meal-plan', 'diet', 'local']

print('Generating 500K+ pages...')

os.makedirs('mega-500k-nutrisystem', exist_ok=True)
count = 0

for i, row in cities_df.iterrows():
    city_slug = row['CITY'].replace(' ', '-').lower()
    state = row['STATE_CODE'].lower()
    
    for zip_mod in zip_multipliers:
        for kw in keywords:
            filename = f'mega-500k-nutrisystem/{city_slug}-{state}-{zip_mod}-{kw}.html'
            
            title = f"Nutrisystem {kw.title()} {row['CITY']} {row['STATE_CODE']} {zip_mod.title()}"
            
            html = f'''<!DOCTYPE html>
<html><head><title>{title}</title>
<meta name="description" content="Nutrisystem {kw} {row['CITY']} {row['STATE_CODE']} {zip_mod}. Local delivery guide.">
</head><body style="padding:20px;max-width:800px;margin:auto">
<h1>{title}</h1>
<p>{row['CITY']} {row['STATE_CODE']} {zip_mod} area | {row['COUNTY']}</p>
<a href="https://convert.ctypy.com/aff_c?offer_id=29197&aff_id=21885" style="background:#ff4757;color:white;padding:15px 30px;display:block;text-decoration:none;font-weight:bold;margin:20px 0">Start Nutrisystem {kw.title()} →</a>
<p style="background:#fff3cd;padding:10px">Affiliate disclosure: Commission earned. Results vary.</p>
<footer>© 2026 TheCreatorVault | {row['CITY']}</footer>
</body></html>'''
            
            with open(filename, 'w') as f:
                f.write(html)
            count += 1
            
            if count % 10000 == 0:
                print(f'Generated {count} pages...')

print(f'✅ MEGA COMPLETE! {count} pages in mega-500k-nutrisystem/')
print('Upload → Sitemap → 10M visits/month potential!')
