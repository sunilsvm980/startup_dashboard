# import streamlit as st
# import pandas as pd
# import time
#
# ##########  TEXT UTILITY   ###############
# # Adding title
# st.title('Startup Dashboard')
# st.header("I am learning sreamlit")
# st.subheader('I am Loving it')
#
# st.write('This is a normal text sample')
#
# st.markdown("""
# ### My favourite movies
# - Race 3
# - Humshakals
# - Housefull
# """)
#
# st.code("""
# def foo(input):
#     return foo**2
# x=foo(2)
# """)
#
# st.latex('x^2+y^2+2=0')
#
#
# #######DISPLAYING ELEMENTS#############
# df=pd.DataFrame({
#     'name':['Nitish','Ankit','Anupam'],
#     'marks':[50,60,70],
#     'package':[10,12,15]
# })
#
# st.dataframe(df)
#
# st.metric('Revenue','RS 3L','3%')
#
# st.json({
#     'name':['Nitish','Ankit','Anupam'],
#     'marks':[50,60,70],
#     'package':[10,12,15]
# })
#
# ######## DISPLAYING MEDIA#############
# st.image('IITK LOGO.jpg')
#
# st.video('video.mp4')
# ##### CREATING LAYOUTS############
#
# st.sidebar.title('Side bar ka title')
#
# col1,col2=st.columns(2)
# with col1:
#     st.image('IITK LOGO.jpg')
# with col2:
#     st.image('IITK LOGO.jpg')
#
# ##########  SHOWING STATUS ############
#
# st.error('Log in Failed')
#
# st.success('Log in successful')
#
# st.info(' You will be directed to a different page')
#
# st.warning('R u sure ? want to log out')
#
# bar=st.progress(0)
# for i in range(1,101):
#     time.sleep((0.01))
#     bar.progress((i))
#
# ########### TAKING USER INPUT################
# email=st.text_input('Enter Email')
# age=st.number_input('Enter age')
# date=st.date_input('Enter registration date')
#
# ##### ADDING BUTTONS  #######
#
# email=st.text_input('Enter Email')
# password=st.text_input('Enter password')
# gender=st.selectbox('Select Gender',['Male','Female','Other'])
#
# btn=st.button('Log in Karo')
# ## if button is clicked
# if btn:
#     if email=='nitish@gmail.com' and password=='1234':
#         st.success('login successful')
#         st.balloons()
#         st.write(gender)
#
#     else:
#         st.error('Login Failed')

#### File uploader ############
# import pandas as pd
# import streamlit as st
#
# file=st.file_uploader('Upload a csv file')
# if file is not None:
#     df=pd.read_csv(file)
#     st.dataframe(df.describe())