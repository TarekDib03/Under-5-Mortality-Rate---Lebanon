# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:05:21 2025

@author: Tarek
"""

# Comparing Lebanon's under-5 mortality with other upper-middle-income countries
countries = ["Lebanon", "Jordan", "Albania", "Armenia", "Peru", "Sri Lanka", "Ukraine", "Global Avg"]
# Approximate 2023 under-5 mortality rates per 1,000 live births (UN IGME/WHO estimates)
rates = [18.2, 14.9, 8.5, 11.3, 12.4, 7.7, 7.5, 37.8]

# Highlight Lebanon
colors = ['#d62728' if country == 'Lebanon' else '#1f77b4' for country in countries]

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
bars = plt.bar(countries, rates, color=colors)
plt.axhline(y=37.8, color='gray', linestyle='--', label='Global Average')

# Add text labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.7, f'{height}', ha='center', va='bottom')

plt.title('Under-5 Mortality Rate (per 1,000 live births) in Upper-Middle-Income Countries – 2023')
plt.ylabel('Deaths per 1,000 live births')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()


