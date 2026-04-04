# 15M PAGE BEAST - generate_15m_nutrisystem.py
import pandas as pd
import os
import itertools

print("🚀 Building 15M page Nutrisystem domination network...")

# MASTER DATA
cities_df = pd.read_csv('https://raw.githubusercontent.com/kelvins/US-Cities-Database/main/csv/us_cities.csv', sep=';')[:5000]
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
neighborhoods = ['north','south','east','west','downtown','uptown','center','main','oldtown','midtown','downtown','hill','valley','ridge','lake','river','park','heights','woods','meadows']
keywords = ['tips','guide','delivery','weightloss','portioncontrol','mealplan','diet','recipes','review','results','cost','vsjennycraig','vsweightwatchers','local','nearme','best','2026','plan','hack','success']

os.makedirs('nutrisystem-empire-15m', exist_ok=True)
count = 0

# 15M COMBINATIONS: 5K cities × 50 states × 10K hoods × 30 keywords
for i, row in cities_df.iterrows():
    city_base = row['CITY'].replace(' ', '-').lower()
    state_code = row['STATE_CODE'].lower()
    
    # STATE VARIATIONS (50x)
    for state in states:
        # NEIGHBORHOOD VARIATIONS (10x)
        for hood in neighborhoods:
            # KEYWORD VARIATIONS (30x)
            for kw in keywords:
                filename = f"nutrisystem-empire-15m/{city_base}-{state}-{hood}-{kw}.html"
                
                title = f"Nutrisystem {kw.title()} {row['CITY']} {state.upper()} {hood.title()}"
                
                html = f'''<!DOCTYPE html>
<html><head>
<title>{title}</title>
<meta name="description" content="Nutrisystem {kw} {row['CITY']} {state.upper()} {hood.title()} area. Local delivery {row['COUNTY']}.">
<script type="application/ld+json">{{"@type":"LocalBusiness","name":"Nutrisystem {row['CITY']} {state}","address":{{"addressLocality":"{row['CITY']}","addressRegion":"{state}"}},"geo":{{"latitude":{row['LATITUDE"]},"longitude":{row['LONGITUDE']}}}}}</script>
</head><body style="max-width:800px;margin:auto;padding:20px;font-family:Arial">
<h1>{title}</h1>
<p><strong>{row['CITY']} {state.upper()} {hood.title()}</strong> | {row['COUNTY']} County | Local Nutrisystem delivery</p>
<p>Portion control meals delivered to your {hood.title()} neighborhood. $12/day. 2-day shipping.</p>
<a href="https://convert.ctypy.com/aff_c?offer_id=29197&aff_id=21885" style="background:#ff4757;color:white;padding:20px 40px;display:block;text-decoration:none;font-weight:bold;font-size:18px;margin:20px 0;text-align:center">Start Nutrisystem {kw.title()} Now →</a>
<div style="background:#fff3cd;padding:15px;margin:20px 0">
<strong>Affiliate Disclosure:</strong> Contains affiliate links. I earn commission at no cost to you. Health results vary - consult physician.
</div>
<footer style="text-align:center;padding:20px;background:#333;color:white">
© 2026 TheCreatorVault | {row['CITY']} {state.upper()} {hood.title()}
</footer>
</body></html>'''
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                count += 1
                
                # Progress
                if count % 50000 == 0:
                    print(f'Generated {count:,} pages... ({count/15_000_000*100:.1f}%)')

print(f'🎉 EMPIRE COMPLETE! {count:,} TOTAL PAGES')
print('📁 Folder: nutrisystem-empire-15m/')
print('🚀 Upload to CDN → Submit sitemap → 100M+ visits/month potential!')
