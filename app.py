import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')
df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],format='mixed')
df['month']=df['date'].dt.month
df['year'] = df['date'].dt.year
######### LOAD OVERALL ANALYSIS #####################
def load_overall_analysis():
    st.title('Overall Analysis')

    ### Total invested amount
    total=round(df['amount'].sum())
    ## Max amount infused in a startup
    max_funding=round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])
    ## Average ticket size
    avg_funding=round(df.groupby('startup')['amount'].sum().mean())
    ## Total funded startup
    num_startup=df['startup'].nunique()


    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' in cr')
    with col2:
        st.metric('Max', str(max_funding) + ' in cr')
    with col3:
        st.metric('Average', str(avg_funding) + ' in cr')
    with col4:
        st.metric('Funded Startup', str(num_startup))
    st.header('MOM graph')
    selected_option=st.selectbox('Select type',['Total','Count'])
    if selected_option=='Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig5)

######### Load investor details #####################
def load_investor_details(investor):
    st.title(investor)
    ## Load recent 5 investment of the investor
    last5_df=df[df['investors'].str.contains(investor)].head(5)[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
     ## Biggest investment
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Biggest Investments')
        fig, ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    with col2:
        ## Sector wise pie chart
        vertical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors wise pie chart')
        fig1, ax = plt.subplots()
        ax.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        ### Stage wise pie chart
        round_series=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Round wise pie chart')
        fig2, ax = plt.subplots()
        ax.pie(round_series, labels=round_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        ### Stage wise pie chart
        city_series=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('City wise pie chart')
        fig3, ax = plt.subplots()
        ax.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    ### YOY investment
    year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('year on year investment line')
    fig4, ax = plt.subplots()
    ax.plot(year_series.index,year_series.values)
    st.pyplot(fig4)


st.sidebar.title('Startup Funding Analysis')
st.session_state.option=st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'],key='analysis')
option=st.session_state.option
if option=='Overall Analysis':
    load_overall_analysis()
elif option=='StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('StartUp Analysis')
else:
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)