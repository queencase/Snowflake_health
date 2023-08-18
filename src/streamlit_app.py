import snowflake.connector
import streamlit as st
import pandas as pd
import numpy as np

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT TABLE_NAME, ROW_COUNT, RETENTION_TIME FROM db_jay.information_schema.tables;")
data = my_cur.fetchall()



#with open("src/custom.html", "r") as f:
#    html_string = f.read()

#st.components.v1.html(html_string)

