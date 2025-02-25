import streamlit as st
import pandas as pd
import numpy as np
import pickle

electronics = pickle.load(open('C:\\Users\\DELL\\Desktop\\Electronic Search Engine\\model\\data.pkl', 'rb'))
similarity=pickle.load(open('C:\\Users\\DELL\\Desktop\\Electronic Search Engine\\model\\similarity.pkl', 'rb'))

def recommendation(product):
    product_index = electronics[electronics['name'] == product].index[0]
    similarity_list = list(enumerate(similarity[product_index]))
    top_10_similar_product = sorted(similarity_list, key=lambda x : x[1], reverse = True)[1:11]

    similar_product = []

    for idx, similary in top_10_similar_product:
        
        product_info={
            'name': electronics.loc[idx]['name'],
            'image': electronics.loc[idx]['image'],
        }

        similar_product.append(product_info)
    return similar_product

st.title('Electronic Search Engine')

product_name=st.selectbox('Select Product', electronics['name'])

if st.button('Search'):
    search_product = recommendation(product_name)
    st.write(f"Top 10 recommended for -> {product_name}")

    for rec in search_product:
        st.image(rec['image'], width=150)
        st.write(f"**{rec['name']}**")
        