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
    ## Sector analysis pie chart
    col5,col6=st.columns(2)
    with col5:
        sectors_sum=df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Sector wise amount pie chart')
        fig6, ax6 = plt.subplots()
        ax6.pie(sectors_sum, labels=sectors_sum.index, autopct="%0.01f%%")
        st.pyplot(fig6)
    with col6:
        sectors_count=df.groupby('vertical')['amount'].count().sort_values(ascending=False).head(5)
        st.subheader('Sector wise count pie chart')
        fig7, ax7 = plt.subplots()
        ax7.barh(sectors_count.index,sectors_count.values)
        st.pyplot(fig7)
    ## type of funding
    st.header('Type of funding')
    funding_type=df.groupby('round')['amount'].sum().sort_values(ascending=False).head(5)
    fig8, ax8 = plt.subplots()
    ax8.bar(funding_type.index, funding_type.values)
    st.pyplot(fig8)

    ## City wise of funding
    st.header('City wise funding')
    funding_city=df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
    fig9, ax9 = plt.subplots()
    ax9.barh(funding_city.index, funding_city.values)
    st.pyplot(fig9)

    ## Funding wise-Overall top 10 startup
    st.header('Fundingwise-Overall top 10 startup')
    top_startup_overall=df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
    fig10, ax10 = plt.subplots()
    ax10.bar(top_startup_overall.index, top_startup_overall.values)
    ax10.set_xticks(ax10.get_xticks(), ax10.get_xticklabels(), rotation=90, ha='right')
    st.pyplot(fig10)

    ## Yearwise top funded startup
    st.header('Yearwise top funded startup')
    new_df = pd.DataFrame(columns=df.columns)
    l1 = list(df.groupby(['year'])['amount'].max().sort_values(ascending=False))
    for i in l1:
        new_df = pd.concat([new_df, df[df['amount'] == i]]).reset_index(drop=True)
    top_startup_year=new_df[['year','startup','amount']].groupby('year').max()
    st.dataframe(top_startup_year)

    ## Top 10 investor
    st.header('Top 10 investor')
    top_investors=df.groupby('investors')['amount'].sum().sort_values(ascending=False).head(10)
    fig11, ax11 = plt.subplots()
    ax11.bar(top_investors.index, top_investors.values)
    ax11.set_xticks(ax10.get_xticks(), ax11.get_xticklabels(), rotation=90, ha='right')
    st.pyplot(fig11)

    st.header('MOM graph')
    selected_option=st.selectbox('Select type',['Total','Count'])
    if selected_option=='Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'],temp_df['amount'])
    ax5.set_xlabel('month on month', fontsize=10)
    # ax5.set_ylabel('Investment in crore', fontsize=10)
    ax5.set_xticks(ax5.get_xticks(), ax5.get_xticklabels(), rotation=90, ha='right')
    plt.xticks(fontsize = 5)
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

def load_company_details(company):
    st.title(company)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Founders', str(company))
    with col2:
        industry=df[df['startup'].str.contains(company)]['vertical'].sort_values(ascending=False).head(1).values[0]
        st.metric('Industry', str(industry))
    with col3:
        subsidiary = df[df['startup'].str.contains(company)]['subvertical'].sort_values(ascending=False).head(1).values[0]
        st.metric('Subsidiary', str(subsidiary))
    with col4:
       city = df[df['startup'].str.contains(company)]['city'].sort_values(ascending=False).head(1).values[0]
       st.metric('Location', str(city))

    st.subheader('Funding Analysis')
    col5,col6=st.columns(2)
    with col5:
        total_funding=df[df['startup'].str.contains('1mg')]['amount'].sum()
        st.metric('Total Funding', str(total_funding))
    with col6:
        stagewise_funding=df[df['startup'].str.contains(company)].groupby('round')['amount'].sum()
        st.subheader('Stagewise funding pie chart')
        fig13, ax13 = plt.subplots()
        ax13.pie(stagewise_funding, labels=stagewise_funding.index, autopct="%0.01f%%")
        st.pyplot(fig13)
    col7,col8=st.columns(2)
    with col7:
        investor_funding=df[df['startup'].str.contains(company)].groupby('investors')['amount'].sum()
        st.subheader('Invetors wise funding')
        fig14, ax14 = plt.subplots()
        ax14.pie(investor_funding, labels=investor_funding.index, autopct="%0.01f%%")
        st.pyplot(fig14)
    with col8:
        date_funding=df[df['startup'].str.contains(company)].groupby('date')['amount'].sum()
        st.subheader('Date wise funding')
        fig15, ax15 = plt.subplots()
        ax15.pie(date_funding, labels=date_funding.index, autopct="%0.01f%%")
        st.pyplot(fig15)



st.sidebar.title('Startup Funding Analysis')
st.session_state.option=st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'],key='analysis')
option=st.session_state.option
if option=='Overall Analysis':
    load_overall_analysis()
elif option=='StartUp':
    selected_company=st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        load_company_details(selected_company)

else:
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)