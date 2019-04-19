# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:37:11 2018

@author: USER
"""
import pyodbc 
import pandas as pd

fetch = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=DESKTOP-5\SQLEXPRESS;"
                        "Database=CCB_DW;"
                        "Trusted_Connection=yes;")
df = pd.read_sql_query('SELECT *   FROM [CCB_DW].[dbo].[DIM_ACCT]', fetch)