from PIL import Image
import requests
from io import BytesIO
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
import wget
import dask
import numpy as np
from glob import glob
import urllib
from typing import Iterable, Union


############ Add a path

def check_or_add(old_path, *args):
    
    """
    This function will help us check whether one or more directories exists, and
    if they don't exist, it will create, combine, and return a new directory.
    """
        
    if not os.path.exists(os.path.join(old_path, *args)):
        os.makedirs(os.path.join(old_path, *args))

    return os.path.join(old_path, *args)

############ Get data func

def get_me_specific_data(
    urls: pd.Series, country_city: str, path_to_files: str, country_city_unique: Iterable, unique_num: Union[int, None] = None
) -> None:
    
    """
    urls: This is a pandas Series with the listings urls in it
    country_city: string with the name of the country or city you would like to get data from
    path_to_file: plain data foldet where the data will go to
    country_city_unique: interable with the unique countries or cities
    unique_num: Default None. If specified, it will download that amount of files
    """
    
    if country_city in country_city_unique: # we go over every country
        
        condition = urls.str.contains(country_city.lower()) # check whether it exists in our list of urls and create a mask
        data_we_need = urls[condition] # we pass that mask to our pandas series
        new_dir = check_or_add(path_to_files, country_city + '_data', 'raw_data') # create a new directory for the raw data
        
        if unique_num: # we first check if a unique number of files was specified
            
            num = 0
            
            while num < unique_num: # loop until we reach that point
                
                try: # we first try to download the file with wget. if wget doesn't work, we try with urllib
                    wget.download(data_we_need.iloc[num], os.path.join(new_dir, f'{country_city}_{num}.csv.gz'))
                except:
                    try: # if urllib doesn't work, we move on to the next one
                        urllib.request.urlretrieve(data_we_need.iloc[num], os.path.join(new_dir, f'{country_city}_{num}.csv.gz'))
                    except:
                        continue
                num += 1
        else:
            
            for num, data in enumerate(data_we_need): # iterate over the links we want
                
                try: # we first try to download the file with wget. if wget doesn't work, we try with urllib
                    wget.download(data, os.path.join(new_dir, f'{country_city}_{num}.csv.gz'))
                except:
                    try: 
                        urllib.request.urlretrieve(data, os.path.join(new_dir, f'{country_city}_{num}.csv.gz'))
                    except:
                        continue
                        

############ decompress csv files


def get_csv_files(data: str, path_out: str, new_dir: str, country_city: str, nums: int) -> None:
    """
    data: the compressed file
    path_out: the directory all of our data for this project
    new_dir: new directory for the uncompressed files
    country_city: name of the country
    nums: number of files available
    """
    
    df = pd.read_csv(data, compression='gzip',  low_memory=False, encoding='utf-8')
    
    df.to_csv(os.path.join(check_or_add(path_out, country_city + '_data', new_dir), 
                                        f'{country_city}_{nums}.csv'), index=False, encoding='utf-8')
    
    print(f"Done Reading and Saving file {nums}!")
    
    

############ get a picture


def image_show(image_url):
    return Image.open(BytesIO(requests.get(image_url).content))