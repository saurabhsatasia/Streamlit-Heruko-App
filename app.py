import streamlit as st
from geopy.geocoders import Nominatim
import pandas as pd
import statsmodels.api as sm
import time
from preprocess import preprocessing
from charts import avg_rating_dist,authors_best,scatter_pages_num_rating,plotly_line_vega,plot_correlation,minmax_norm_dist
from charts import mean_norm_dist,all_three_dist,norm_comparison, awards_boxplot,yearly_minmax_mean,minmax_awards
from charts import place_title
from bg import set_png_as_page_bg

def st_app(df_read):
    set_png_as_page_bg('hog.jpg')
    bgcolor = st.color_picker("Pick a Background color")
    fontcolor = st.color_picker("Pick a Font Color", "#fff")

    html_temp_1 = """<div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center;">{}</h1>
    </div>"""
    html_temp_2 = """<div style="background-color:#54545A;padding:4px">
        <h4 style="color:#6CF906;text-align:center;">{} </h4>
        </div>"""
    html_temp_3 = """<div style="background-color:#54545A;padding:4px">
            <h3 style="color:#EFF5F5;text-align:center;">{} </h3>
            </div>"""
    st.markdown(html_temp_1.format(bgcolor, fontcolor,"Team : McGonagall"), unsafe_allow_html=True)
    # st.markdown("""<div><p style='color:{}'>Hello Strive</p></div>""".format(bgcolor), unsafe_allow_html=True)
    # st.title("Team : McGonagall")
    st.sidebar.selectbox("Choose", ['Project', 'About'])
    st.markdown(html_temp_1.format(bgcolor, fontcolor,"Task --> Best books of the decade:2000 "), unsafe_allow_html=True)
    #columns = ['Title', 'Author', 'minirating', 'num_reviews', 'num_pages', 'awards', 'genres', 'series', 'year_published', 'places']

    df = preprocessing(df=df_read)
    df=df.drop("Title_URL", axis=1)
    my_bar = st.progress(0)
    if st.button("Generate Data"):
        with st.spinner("Waiting .."):
            for p in range(0, 120, 20):
                time.sleep(0.1)
                my_bar = my_bar.progress(p)
            st.dataframe(df.style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'}))
            st.success("Generated Dataframe")
    # ANALYSIS
    ## EX-1
    st.markdown(html_temp_3.format("ANALYSIS"),unsafe_allow_html=True)
    str1= "Group the books by `original_publish_year` and get the mean of the `minmax_norm_ratings` of the groups."
    st.markdown(html_temp_2.format(str1),unsafe_allow_html=True)
    # st.info("""### *1. Group the books by `original_publish_year` and get the mean of the `minmax_norm_ratings` of the groups.*""")
    groupby_minmax = df.groupby('year_published').agg({'minmax_norm_rating':'mean'})
    col1, col2 = st.beta_columns([2,4])
    groupby_minmax = groupby_minmax.style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'})
    with col1: st.dataframe(groupby_minmax)
    with col2:
        if st.button("PLOT"):
            st.area_chart(groupby_minmax)

    # EX-2
    str2= 'Create a function that given an author as input it returns her/his book with the highest minmax_norm_ratings.'
    st.markdown(html_temp_2.format(str2),unsafe_allow_html=True)
    # st.info("""### *2. Create a function that given an author as input it returns her/his book with the highest minmax_norm_ratings.*""")
    col3,col4 = st.beta_columns(2)
    with col3: auth = st.selectbox("Select Author", df['Author'].unique().tolist())
    with col4: st.success(authors_best(auth, df))

    st.markdown(html_temp_3.format("VISUALIZATION"),unsafe_allow_html=True)
    # st.subheader("VISUALIZATION")
    # EX-1
    str3='Create a 2D scatterplot with `pages` on the x-axis and `num_ratings` on the y-axis.'
    st.markdown(html_temp_2.format(str3),unsafe_allow_html=True)
    # st.info("""### *1. Create a 2D scatterplot with `pages` on the x-axis and `num_ratings` on the y-axis.*""")
    ex_1 = scatter_pages_num_rating(df)
    st.plotly_chart(ex_1)
    st.subheader("Same plot using Streamlit-line_vega_chart")
    plotly_line_vega(df)

    # EX-2
    str4='Can you compute numerically the correlation coefficient of these two columns?'
    st.markdown(html_temp_2.format(str4),unsafe_allow_html=True)
    # st.info("""### *2. Can you compute numerically the correlation coefficient of these two columns?* """)
    st.write(plot_correlation(df))

    # EX-3
    str5 = 'Visualise the `avg_rating` distribution.'
    st.markdown(html_temp_2.format(str5),unsafe_allow_html=True)
    # st.info("""### *3. Visualise the `avg_rating` distribution.*""")
    ex_3 = avg_rating_dist(df)
    st.plotly_chart(ex_3)

    # EX-4
    str6 = 'Visualise the `minmax_norm_rating` distribution.'
    st.markdown(html_temp_2.format(str6),unsafe_allow_html=True)
    # st.info("""### *4. Visualise the `minmax_norm_rating` distribution.*""")
    st.plotly_chart(minmax_norm_dist(df))

    # EX-5
    str7 = 'Visualise the `mean_norm_rating` distribution.'
    st.markdown(html_temp_2.format(str7),unsafe_allow_html=True)
    # st.info("""### *5. Visualise the `mean_norm_rating` distribution.*""")
    st.plotly_chart(mean_norm_dist(df))
    st.subheader("All distribution in one!!")
    st.plotly_chart(all_three_dist(df))

    # EX-6
    str8 = 'Create one graph that represents in the same figure both `minmax_norm_rating` and `mean_norm_rating` distributions.'
    st.markdown(html_temp_2.format(str8),unsafe_allow_html=True)
    # st.info("""### *6. Create one graph that represents in the same figure both `minmax_norm_rating` and `mean_norm_rating` distributions.*""")
    st.plotly_chart(norm_comparison(df))

    # EX-8
    str9 = 'Visualize the awards distribution in a boxplot and aggregtated bars.'
    st.markdown(html_temp_2.format(str9),unsafe_allow_html=True)
    # st.info("""### *8. Visualize the awards distribution in a boxplot and aggregtated bars.*""")
    st.plotly_chart(awards_boxplot(df))

    # EX-9
    str10 = 'Group the `books` by `original_publish_year` and get the mean of the `minmax_norm_ratings` of the groups.'
    st.markdown(html_temp_2.format(str10),unsafe_allow_html=True)
    # st.info("""### *9. Group the `books` by `original_publish_year` and get the mean of the `minmax_norm_ratings` of the groups.*""")
    st.plotly_chart(yearly_minmax_mean(df))

    # EX-10
    str11 = 'Make a scatterplot to represent minmax_norm_ratings in function of the number of awards won by the book.'
    st.markdown(html_temp_2.format(str11),unsafe_allow_html=True)
    # st.info("""### *10. Make a scatterplot to represent minmax_norm_ratings in function of the number of awards won by the book.*""")
    st.plotly_chart(minmax_awards(df))  #
    # st.pyplot(minmax_awards_2(df,fig_size=(10,10))) ## Old matplotlib plot

    # EX-7 Not working
    # str12='What is the best fit in terms of a distribution (normal, chi-squared...) to represent each of those graphs?'
    # st.markdown(html_temp_2.format(str12), unsafe_allow_html=True)
    # st.image("D:/Strive/st/goodreads_best2000-main/pngs/distribution_fit.png")

    # Explore maps in streamlit
    str_m = "Books and Places."
    st.markdown(html_temp_2.format(str_m), unsafe_allow_html=True)
    book = st.selectbox("Select Book", df['Title'].unique())
    df_res = pd.DataFrame(place_title(book,df))
    place = st.write(df_res.style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'}))
    """### *Type the Location you received above*"""
    where = st.text_area("\n" ," Type here...")
    if st.button("Submit"):
        geolocator = Nominatim(user_agent="a")
        location = geolocator.geocode(where)
        lat = location.latitude
        lon = location.longitude
        map_df = pd.DataFrame.from_dict({"lat": [lat], "lon": [lon]})
        st.map(map_df)



def main():
    df_read = pd.read_csv("D:/Strive/Streamlit-Heruko-App/Best_2000s.csv")
    st_app(df_read)


if __name__ == '__main__':
    main()