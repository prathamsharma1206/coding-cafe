import os
import json
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'data', 'ad-engagements.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('='):].lstrip('=').strip()
raw_data = json.loads(json_str)

matched_ads_count = 0
advertisers = []

for item in raw_data:
    try:
        # Navigate down to engagements list
        engagements_wrapper = item['ad']['adsUserData']['adEngagements']
        # adEngagements can be a dict containing 'engagements' or a list itself
        engagements = engagements_wrapper.get('engagements', []) if isinstance(engagements_wrapper, dict) else engagements_wrapper
        
        for engagement in engagements:
            targeting_criteria = engagement.get('matchedTargetingCriteria', [])
            match_found = False
            for criterion in targeting_criteria:
                # Check for targetingType 'Keywords' and targetingValue 'AI'
                if (criterion.get('targetingType') == 'Keywords' and 
                    criterion.get('targetingValue') == 'AI'):
                    match_found = True
                    break
            
            if match_found:
                matched_ads_count += 1
                advertiser_info = engagement.get('advertiserInfo', {})
                adv_name = advertiser_info.get('advertiserName')
                if adv_name:
                    advertisers.append(adv_name)
    except (KeyError, TypeError) as e:
        continue

print(f"1. Ads matched: {matched_ads_count}")
print(f"2. Unique advertisers: {len(set(advertisers))}")
if advertisers:
    counts = Counter(advertisers)
    print(f"3. Top advertiser: {counts.most_common(1)[0]}")
else:
    print("3. No advertisers found.")