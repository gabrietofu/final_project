import streamlit as st
import pandas as pd
import random
import pydeck as pdk

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'store_name' not in st.session_state:
    st.session_state.store_name = ''

def button_click(page):
    st.session_state.page = page

def button_click_2(page,store_name):
    st.session_state.page = page
    st.session_state.store_name = store_name

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:url("https://i.imgur.com/wtY58mv.png");
            background-attachment:fixed;
            background-size:cover
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()

    
# 1번 슬라이드
def home_page():
    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 200px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        }
        </style>
        """, unsafe_allow_html=True
    )
 # padding: 요소의 내부 여백
 # 2px: 테두리의 너비 / solid: 스타일

    title = "Hi Bread!"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)  

    subheader = "어떤 곳을 찾고있어?"
    html_temp = f"""
    <div style="text-align: center;">
        <h1 style="color: black; font-size: 20px;">{subheader}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button('**평범해요~**',on_click=button_click,args=("cluster_0",),key="button_1")
        st.button('**빵이 맛있어요!**',on_click=button_click,args=("cluster_1",),key="button_2")

    with col2:
        st.button('**가성비 맛집이에요!**',on_click=button_click,args=("cluster_2",),key="button_3")
        st.button('**다소 비싸지만 값어치해요!**',on_click=button_click,args=("cluster_4",),key="button_4")

    with col3:
        st.button('**풍경과 분위기가 좋아요!**',on_click=button_click,args=("cluster_3",),key="button_5")

# 2번 슬라이드로 이동하는 함수
def cluster_0():
    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 160px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        }
        </style>
        """, unsafe_allow_html=True
    )

    title = "누구 만나보고 싶어?"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_mode = pd.read_csv('streamlit_mode.csv')
    df_mode_0 = df_mode[df_mode['cluster']==0]
    df_mode_0_values = sorted(df_mode_0['Store'].values)
    store_list_0 = random.sample(df_mode_0_values, 8)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(f'**{store_list_0[0]}**',on_click=button_click_2,args=("cluster_0_store0", store_list_0[0],),key="button_7")
        st.button(f'**{store_list_0[1]}**',on_click=button_click_2,args=("cluster_0_store1", store_list_0[1],),key="button_8")
        st.button("(뒤로가기)", on_click=button_click, args=("home",))
    with col2:
        st.button(f'**{store_list_0[2]}**',on_click=button_click_2,args=("cluster_0_store2", store_list_0[2],),key="button_9")
        st.button(f'**{store_list_0[3]}**',on_click=button_click_2,args=("cluster_0_store3", store_list_0[3],),key="button_10")
    with col3:
        st.button(f'**{store_list_0[4]}**',on_click=button_click_2,args=("cluster_0_store4", store_list_0[4],),key="button_11")
        st.button(f'**{store_list_0[5]}**',on_click=button_click_2,args=("cluster_0_store5", store_list_0[5],),key="button_12")

    with col4:
        st.button(f'**{store_list_0[6]}**',on_click=button_click_2,args=("cluster_0_store6", store_list_0[6],),key="button_13")
        st.button(f'**{store_list_0[7]}**',on_click=button_click_2,args=("cluster_0_store7", store_list_0[7],),key="button_14")

def cluster_1():

    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 160px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        </style>
        """, unsafe_allow_html=True
    )

    title = "누구 만나보고 싶어?"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_mode = pd.read_csv('streamlit_mode.csv')
    df_mode_1 = df_mode[df_mode['cluster']==1]
    df_mode_1_values = sorted(df_mode_1['Store'].values)
    store_list_1 = random.sample(df_mode_1_values, 8)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(f'**{store_list_1[0]}**', on_click=button_click_2, args=("cluster_1_store0", store_list_1[0],),key="button_15")
        st.button(f'**{store_list_1[1]}**', on_click=button_click_2, args=("cluster_1_store1", store_list_1[1],),key="button_16")
        st.button("(뒤로가기)", on_click=button_click, args=("home",))
    with col2:
        st.button(f'**{store_list_1[2]}**', on_click=button_click_2, args=("cluster_1_store2", store_list_1[2],),key="button_17")
        st.button(f'**{store_list_1[3]}**', on_click=button_click_2, args=("cluster_1_store3", store_list_1[3],),key="button_18")
    with col3:
        st.button(f'**{store_list_1[4]}**', on_click=button_click_2, args=("cluster_1_store4", store_list_1[4],),key="button_19")
        st.button(f'**{store_list_1[5]}**', on_click=button_click_2, args=("cluster_1_store5", store_list_1[5],),key="button_20")
    with col4:
        st.button(f'**{store_list_1[6]}**', on_click=button_click_2, args=("cluster_1_store6", store_list_1[6],),key="button_21")
        st.button(f'**{store_list_1[7]}**', on_click=button_click_2, args=("cluster_1_store7", store_list_1[7],),key="button_22")


def cluster_2():

    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 160px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        }
        </style>
        """, unsafe_allow_html=True
    )

    title = "누구 만나보고 싶어?"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_mode = pd.read_csv('streamlit_mode.csv')
    df_mode_2 = df_mode[df_mode['cluster']==2]
    df_mode_2_values = sorted(df_mode_2['Store'].values)
    store_list_2 = random.sample(df_mode_2_values, 8)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(f'**{store_list_2[0]}**', on_click=button_click_2, args=("cluster_2_store0", store_list_2[0],),key="button_23")
        st.button(f'**{store_list_2[1]}**', on_click=button_click_2, args=("cluster_2_store1", store_list_2[1],),key="button_24")
        st.button("(뒤로가기)", on_click=button_click, args=("home",))
    with col2:
        st.button(f'**{store_list_2[2]}**', on_click=button_click_2, args=("cluster_2_store2", store_list_2[2],),key="button_25")
        st.button(f'**{store_list_2[3]}**', on_click=button_click_2, args=("cluster_2_store3", store_list_2[3],),key="button_26")
    with col3:
        st.button(f'**{store_list_2[4]}**', on_click=button_click_2, args=("cluster_2_store4", store_list_2[4],),key="button_27")
        st.button(f'**{store_list_2[5]}**', on_click=button_click_2, args=("cluster_2_store5", store_list_2[5],),key="button_28")
    with col4:
        st.button(f'**{store_list_2[6]}**', on_click=button_click_2, args=("cluster_2_store6", store_list_2[6],),key="button_29")
        st.button(f'**{store_list_2[7]}**', on_click=button_click_2, args=("cluster_2_store7", store_list_2[7],),key="button_30")

def cluster_3():

    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 160px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        }
        </style>
        """, unsafe_allow_html=True
    )

    title = "누구 만나보고 싶어?"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_mode = pd.read_csv('streamlit_mode.csv')
    df_mode_3 = df_mode[df_mode['cluster']==3]
    store_3 = df_mode_3['Store'].tolist()

    df_mode_3_values = sorted(df_mode_3['Store'].values)
    store_list_3 = random.sample(df_mode_3_values, 3)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(f'**{store_list_3[0]}**', on_click=button_click_2, args=("cluster_3_store0", store_list_3[0],),key="button_31")
        st.button(f'**{store_list_3[1]}**', on_click=button_click_2, args=("cluster_3_store1", store_list_3[1],),key="button_32")

    with col2:
        st.button(f'**{store_list_3[2]}**', on_click=button_click_2, args=("cluster_3_store2", store_list_3[2],),key="button_33")
        st.button("(뒤로가기)", on_click=button_click, args=("home",))

def cluster_4():
    st.markdown("""
        <style>
        .stButton>button {
            color: black;
            text_align: center;
            background-color: #ffffff;
            padding: 10px 24px;
            border: 3px solid black;
            border-raius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 160px;
            height: 80px;
        }
        .stButton>button:hover {
            background-color: #ebebeb;
        }
        </style>
        """, unsafe_allow_html=True
    )

    title = "누구 만나보고 싶어?"
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f2b879; font-size: 55px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_mode = pd.read_csv('streamlit_mode.csv')
    df_mode_4 = df_mode[df_mode['cluster']==4]
    store_4 = df_mode_4['Store'].tolist()

    st.button(f'**{store_4[0]}**', on_click=button_click_2, args=("cluster_4_store", store_4[0],),key="button_39")
    st.button("(뒤로가기)", on_click=button_click, args=("home",))

# 3번 슬라이드(cluster_0)
def cluster_0_store0():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store1():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store2():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store3():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store4():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store5():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store6():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_0_store7():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_0",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

# 3번 슬라이드(cluster_1)
def cluster_1_store0():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store1():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store2():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store3():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store4():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store5():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store6():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_1_store7():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_1",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store0():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store1():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store2():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store3():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store4():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store5():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store6():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_2_store7():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_2",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_3_store0():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid black;
        border-raius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 160px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_3",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_3_store1():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_3",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_3_store2():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    good_review = df_text[(df_text['sentiment']==1) & (df_text['Store']==store_name)]['Review_text']
    good_review = sorted(good_review.values)

    if len(good_review) == 0:
        good_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(good_review) == 1:
        random_review = random.sample(good_review, 1)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 2:
        random_review = random.sample(good_review, 2)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 3:
        random_review = random.sample(good_review, 3)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(good_review) == 4:
        random_review = random.sample(good_review, 4)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(good_review, 5)
        good_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    if len(bad_review) == 0:
        bad_review_text = pd.DataFrame({"Review" : ["리뷰가 없어요!"]})
    elif len(bad_review) == 1:
        random_review = random.sample(bad_review, 1)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})    
    elif len(bad_review) == 2:
        random_review = random.sample(bad_review, 2)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 3:
        random_review = random.sample(bad_review, 3)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    elif len(bad_review) == 4:
        random_review = random.sample(bad_review, 4)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review})
    else:
        random_review = random.sample(bad_review, 5)
        bad_review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : random_review}) 

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_3",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)


        # 긍정 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(good_review_text)

        # 부정 리뷰
        subheader_html = """
            <style>
            .subheader h3{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h3>저의 단점은😭</h3>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)       

        st.dataframe(bad_review_text)

def cluster_4_store0():
    st.markdown("""
    <style>
    .stButton>button {
        color: black;
        text_align: center;
        background-color: #ffffff;
        padding: 10px 24px;
        border: 3px solid #c2c2c2;
        border-raius: 8px;
        cursor: pointer;
        font-size: 20px !important;
        width: 345px;
        height: 80px;
    }
    .stButton>button:hover {
        background-color: #ebebeb;
    }
    </style>
    """, unsafe_allow_html=True
    )

    title = st.session_state.store_name
    html_temp = f"""
    <div style="text-align: center; margin: 40px;">
        <h1 style="color: #f5bf84; font-size: 45px; text-shadow: -1px -1px 2px #d4833b,\
          1px -1px 2px #d4833b, -1px 1px 2px #d4833b, 1px 1px 2px #d4833b;">{title}</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    store_name = st.session_state.store_name
    
    df_text = pd.read_csv('streamlit_text.csv')


    # 빵집 정보
    df_info = pd.DataFrame({"feature" : ["이름", "사는곳", "성격", "성적"],\
                             "info" : [store_name, df_text[df_text['Store']==store_name]['Address'].iloc[0], \
                            df_text[df_text['Store']==store_name]['cluster_labeling'].iloc[0],\
                            df_text[df_text['Store']==store_name]['Review_score'].iloc[0]]})
    
    # 긍정 리뷰
    review = df_text[df_text['Store']==store_name]['Review_text']
    review_text = pd.DataFrame({"Review(리뷰 더블 클릭!!!)" : review})

    # 부정 리뷰
    bad_review = df_text[(df_text['sentiment']==0) & (df_text['Store']==store_name)]['Review_text']
    bad_review = sorted(bad_review.values)

    # 경도
    log = df_text[df_text['Store']==store_name]['X'].values[0]
    # 위도
    lat = df_text[df_text['Store']==store_name]['Y'].values[0]

    test = pd.DataFrame({"lat" : lat, "log" : log}, index=[0])

    col1, col2 = st.columns(2)   

    with col1:
        # pydeck을 이용한 지도 생성
        layer = pdk.Layer(
            'ScatterplotLayer',
            test,
            get_position='[log, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20,
        )

        # 뷰 상태 정의
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=log,
            zoom=15,
        )

        # pydeck 차트 생성
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v10')
        st.pydeck_chart(r)
    
        st.button("다른 친구 보러가기", on_click=button_click, args=("cluster_4",))

    with col2:
        # 식당 정보 입력
        subheader_html = """
            <style>
            .subheader h1{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h1>저를 소개할께요😊</h1>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(df_info)

        # 리뷰
        subheader_html = """
            <style>
            .subheader h2{
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border: 5px outset;
                border-raius: 20px;
                text-align: center;
                font-size: 15px !important;
                width: 345px;
                height: 40px;
                margin-bottom: 3px;
            }
            </style>
            <div class="subheader">
                <h2>저의 장점은😍</h2>
            </div>
        """
        st.markdown(subheader_html, unsafe_allow_html=True)

        st.dataframe(review_text)


# 페이지 렌더링(홈페이지)
if st.session_state.page == 'home':
    print(st.session_state.page)
    home_page()

# 페이지 렌더링(slide 2)
elif st.session_state.page == 'cluster_0':
    print(st.session_state.page)
    cluster_0()

elif st.session_state.page == 'cluster_1':
    print(st.session_state.page)
    cluster_1()

elif st.session_state.page == 'cluster_2':
    print(st.session_state.page)
    cluster_2()    

elif st.session_state.page == 'cluster_3':
    print(st.session_state.page)
    cluster_3()    

elif st.session_state.page == 'cluster_4':
    print(st.session_state.page)
    cluster_4()    

# 페이지 렌더링(slide 3 - cluster0)
elif st.session_state.page == 'cluster_0_store0':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store0()

elif st.session_state.page == 'cluster_0_store1':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store1()    

elif st.session_state.page == 'cluster_0_store2':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store2()    

elif st.session_state.page == 'cluster_0_store3':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store3()    

elif st.session_state.page == 'cluster_0_store4':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store4()

elif st.session_state.page == 'cluster_0_store5':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store5()    

elif st.session_state.page == 'cluster_0_store6':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store6()    

elif st.session_state.page == 'cluster_0_store7':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_0_store7()

# 페이지 렌더링(slide 3 - cluster1)
elif st.session_state.page == 'cluster_1_store0':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store0()

elif st.session_state.page == 'cluster_1_store1':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store1()    

elif st.session_state.page == 'cluster_1_store2':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store2()    

elif st.session_state.page == 'cluster_1_store3':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store3()    

elif st.session_state.page == 'cluster_1_store4':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store4()

elif st.session_state.page == 'cluster_1_store5':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store5()    

elif st.session_state.page == 'cluster_1_store6':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store6()    

elif st.session_state.page == 'cluster_1_store7':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_1_store7()

# 페이지 렌더링(slide 3 - cluster2)
elif st.session_state.page == 'cluster_2_store0':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store0()

elif st.session_state.page == 'cluster_2_store1':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store1()    

elif st.session_state.page == 'cluster_2_store2':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store2()    

elif st.session_state.page == 'cluster_2_store3':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store3()    

elif st.session_state.page == 'cluster_2_store4':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store4()

elif st.session_state.page == 'cluster_2_store5':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store5()    

elif st.session_state.page == 'cluster_2_store6':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store6()    

elif st.session_state.page == 'cluster_2_store7':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_2_store7()

# 페이지 렌더링(slide 3 - cluster3)
elif st.session_state.page == 'cluster_3_store0':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_3_store0()

elif st.session_state.page == 'cluster_3_store1':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_3_store1()    

elif st.session_state.page == 'cluster_3_store2':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_3_store2()

# 페이지 렌더링(slide 3 - cluster4)
elif st.session_state.page == 'cluster_4_store':
    print(f"{st.session_state.page} & {st.session_state.store_name}")
    cluster_4_store0()