from jpndlpy import JapanNdlClient
import collections
import pandas as pd
import os
import re

jndlclient = JapanNdlClient()

start_year = 1980
last_year = 2021
ndc = 007.64

def get(start_year, last_year, ndc):
    ndc = str(ndc)
    X = 0
    for i in range(start_year, last_year ):
        cntc = 500
        idxc = 1
        title_list = []
        while X < 3:
            response = jndlclient.search_text(title="", ndc=ndc, from_date=str(i), until_date=str(i), cnt=cntc,
                                              idx=idxc)
            res = response.to_json()
            title_new = []
            for i in res["items"]:
                title_list.append(i["title"].replace('\u3000', ''))
                title_new.append(i["title"].replace('\u3000', ''))
