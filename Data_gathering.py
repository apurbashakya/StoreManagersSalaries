# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:10:10 2021

@author: User
"""

import glassdoor_scraper as gs
import pandas as pd
path = r"C:/Users/User/Documents/Github/StoreManagersSalaries/chromedriver"
df = gs.get_jobs('Store managers',15, False, path, 20)
df.to_csv ('StoreManagers.csv', index = False, header=True)