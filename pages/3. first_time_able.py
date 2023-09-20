# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:12:45 2023

plotting three column inputs (ID_period_value format) that depicting first time a site being treated/infested/detectable/propagules

q.txt
u.txt
v.txt
z.txt

produce four static maps
option to input a scenario name
option to select colorscheme (maybe separately for each plt at a later time)

@author: nliu
"""
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import pandas as pd

#layout setting
st.set_page_config(layout="wide")
#Load your x-y data - path 
xcoord = pd.read_csv('input/x_coord.txt', sep = '\t', header = None, names = ['gridID', 'x'])
ycoord = pd.read_csv('input/y_coord.txt', sep = '\t', header = None, names = ['gridID', 'y'])
xcoord = xcoord.merge(ycoord, on = 'gridID', how = 'left')

# joining geometry with NodeID - value format input 
def join_geom(file, geom = xcoord, **kwargs):
    data = pd.read_csv(file, sep = '\t', header = None, names = ['gridID', 'period', 'value'])
    data = geom.merge(data, on = 'gridID', how = 'right')
    return data#, len(set(data['period']))

def first_time(data):
    data = data.sort_values('period')
    data.drop_duplicates(subset='gridID', keep='first', inplace=True)
    return data

def get_color(cmap, iter):
    palette = list(reversed(sns.color_palette(cmap, iter).as_hex()))
    return palette

# dict = {'q.txt': 'first treated', 'u.txt': 'first infested', 'v.txt': 'first detectable', 'z.txt': 'first spread propagules'}
# # Define marker symbols for different insect density values
marker_symbols = ['.', 'o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
uploaded_files = st.file_uploader(label = 'select files', type = ['txt', 'csv'], accept_multiple_files=True)
st.subheader('Recommend to upload q.txt, u.txt, v.txt, and z.txt only')
st.write(pd.DataFrame({'file name': ['q', 'u', 'v', 'z'], 'meaning': ['treated', 'infested', 'detectable', 'spread propagules'],}))

# define color scheme
colorScheme = st.selectbox('Select color palette', ('Paired', "viridis",'Spectral', 'Set2'))
if colorScheme is not None:
    period_palette = get_color(colorScheme,16)

confirmButton = st.button('Confirm')

col1, col2 = st.columns(2)
if confirmButton:
    for uploaded_file in uploaded_files: 
        with col1:
            if uploaded_file.id == 1:
                data = first_time(join_geom(uploaded_file))
                fig, ax = plt.subplots()
                for i in set(data['period']):
                    data_i = data.loc[data['period'] == i]
                    ax.scatter(x=data_i['x'], y=data_i['y'], c=period_palette[i], marker=marker_symbols[i], label=i, edgecolors='none')
                plt.xlim(-1300000, -800000)
                plt.ylim(7290000, 7850000)
                ax.legend()
                plt.axis('off')
                plt.title(uploaded_file.name)
                st.pyplot(fig)

        with col2:
            if uploaded_file.id == 2:
                data = first_time(join_geom(uploaded_file))
                fig, ax = plt.subplots()
                for i in set(data['period']):
                    data_i = data.loc[data['period'] == i]
                    ax.scatter(x=data_i['x'], y=data_i['y'], c=period_palette[i], marker=marker_symbols[i], label=i, edgecolors='none')
                plt.xlim(-1300000, -800000)
                plt.ylim(7290000, 7850000)
                # ax.legend()
                plt.axis('off')
                plt.title(uploaded_file.name)
                st.pyplot(fig)

        with col1:
            if uploaded_file.id == 3:
                data = first_time(join_geom(uploaded_file))
                fig, ax = plt.subplots()
                for i in set(data['period']):
                    data_i = data.loc[data['period'] == i]
                    ax.scatter(x=data_i['x'], y=data_i['y'], c=period_palette[i], marker=marker_symbols[i], label=i, edgecolors='none')
                plt.xlim(-1300000, -800000)
                plt.ylim(7290000, 7850000)
                ax.legend()
                plt.axis('off')
                plt.title(uploaded_file.name)
                st.pyplot(fig)

        with col2:
            if uploaded_file.id == 4:
                data = first_time(join_geom(uploaded_file))
                fig, ax = plt.subplots()
                for i in set(data['period']):
                    data_i = data.loc[data['period'] == i]
                    ax.scatter(x=data_i['x'], y=data_i['y'], c=period_palette[i], marker=marker_symbols[i], label=i, edgecolors='none')
                plt.xlim(-1300000, -800000)
                plt.ylim(7290000, 7850000)
                # ax.legend()
                plt.axis('off')
                plt.title(uploaded_file.name)
                st.pyplot(fig)