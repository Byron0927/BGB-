import streamlit as st

#emoji sources: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="漢堡巴士路線資料", page_icon=":Oncoming Bus:", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Source+Han+Sans+TC:wght@400;500&display=swap');

    /* 設定全局字體 */
    body {
        font-family: 'Source Han Sans TC', 'Roboto', sans-serif;
    }

    /* 你也可以自定義特定區域的字體 */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
    }

    p {
        font-family: 'Source Han Sans TC', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True
)


# ---- HEADER SECTIONS ----

with st.container():
    st.title("漢堡巴士路線")
    st.subheader("可在此查閱漢堡巴士各路線的詳細資料。")
    st.write("[可參考 >](https://docs.google.com/spreadsheets/d/1_hF_4ObI7j7OKKa__Bs9-fCLS6jYLvtTxg_nzhzkLjU/edit?gid=956048970#gid=956048970)")

# 創建兩欄 (左 2 右 3)
col1, col2 = st.columns([2, 3])

# ---- ROUTES DETAILS ----

#路線方向
route_directions = {
    "1": ["1_MAF1", "1_MAF2", "1_HVU1", "1_HVU2", "1_HVU3"]}

#車站資料
route_stops = {
    "1_MAF1": ["1.跑馬地 (上)，蟠龍道", "2.箕鏈坊，藍塘道", "3.桂芳街，成和道", "4.山村道，成和道", "5.景光街",
             "6.養和醫院，黃泥涌道", "7.跑馬地馬場，黃泥涌道", "8.立德里，摩利臣山道", "9.利景酒店，灣仔道",
             "10.普樂里，灣仔道", "11.修頓球場，軒尼詩道", "12.晏頓街，軒尼詩道", "13.金鐘 - 太古廣場，金鐘道",
             "14.中銀大廈，金鐘道", "15.置地廣場，德輔道中", "16.中環街市，德輔道中", "17.急庇利街，德輔道中",
             "18.上環 - 港澳碼頭"],

    "1_MAF2": ["1.跑馬地 (上)，蟠龍道", "2.箕鏈坊，藍塘道", "3.桂芳街，成和道", "4.山村道，成和道", "5.景光街",
             "6.養和醫院，黃泥涌道", "7.立德里，摩利臣山道", "8.利景酒店，灣仔道", "9.普樂里，灣仔道",
             "10.修頓球場，軒尼詩道", "11.晏頓街，軒尼詩道", "12.金鐘 - 太古廣場，金鐘道",
             "13.中銀大廈，金鐘道", "14.置地廣場，德輔道中", "15.中環街市，德輔道中", "16.急庇利街，德輔道中",
             "17.上環 - 港澳碼頭"],
    "1_HVU1": ["1.上環 - 港澳碼頭", "2.林士街，德輔道中", "3.恒生銀行總行大廈，德輔道中", "4.德忌利士街，德輔道中", 
             "5.皇后像廣場 ，遮打道", "6.金鐘 - 金鐘廊，金鐘道", "7.軍器廠街，軒尼詩道", "8.柯布連道，軒尼詩道", 
             "9.譚臣道，菲林明道", "10.克街，灣仔道", "11.天樂里，灣仔道", "12.樂活道，黃泥涌道", 
             "13.雅谷大廈，黃泥涌道", "14.跑馬地（下），黃泥涌道", "15.奕蔭街，成和道", "16.昇平樓，成和道", 
             "17.箕鏈坊，藍塘道", "18.跑馬地 (上)，蟠龍道"],
    "1_HVU2": ["1.上環 - 港澳碼頭", "2.林士街，德輔道中", "3.恒生銀行總行大廈，德輔道中", "4.德忌利士街，德輔道中", 
             "5.歷山大廈，德輔道中", "6.遮打花園，德輔道中", "7.金鐘 - 金鐘廊，金鐘道", "8.軍器廠街，軒尼詩道", "9.柯布連道，軒尼詩道", 
             "10.譚臣道，菲林明道", "11.克街，灣仔道", "12.天樂里，灣仔道", "13.樂活道，黃泥涌道", 
             "14.雅谷大廈，黃泥涌道", "15.跑馬地（下），黃泥涌道", "16.奕蔭街，成和道", "17.昇平樓，成和道", 
             "18.箕鏈坊，藍塘道", "19.跑馬地 (上)，蟠龍道"],
    "1_HVU3": ["1.上環 - 港澳碼頭", "2.林士街，德輔道中", "3.恒生銀行總行大廈，德輔道中", "4.德忌利士街，德輔道中", 
             "5.皇后像廣場 ，遮打道", "6.金鐘 - 金鐘廊，金鐘道", "7.軍器廠街，軒尼詩道", "8.柯布連道，軒尼詩道", 
             "9.譚臣道，菲林明道", "10.克街，灣仔道", "11.天樂里，灣仔道", "12.樂活道，黃泥涌道", 
             "13.雅谷大廈，黃泥涌道", "14.跑馬地（下），黃泥涌道", "15.奕蔭街，成和道", "16.昇平樓，成和道", 
             "17.箕鏈坊，藍塘道", "18.跑馬地 (上)，蟠龍道"]
             }
    
#車資
route_fare = {
             "1_MAF1":["跑馬地 (上)，蟠龍道 起 $9"],
             "1_MAF2":["跑馬地 (上)，蟠龍道 起 $9"],
             "1_HVU1":["上環-港澳碼頭 起 $9"],
             "1_HVU2":["上環-港澳碼頭 起 $9"],
             "1_HVU3":["上環-港澳碼頭 起 $9"],
             }

#服務時間
route_service_time = {
    "1_MAF1": "06:00 - 23:00",
    "1_MAF2": "06:00 - 23:00，只於跑馬日服務",
    "1_HVU1": "06:30 - 23:30，星期一至五，公眾假期除外",
    "1_HVU2": "06:30 - 23:30，星期六、日及公眾假期",
    "1_HVU3": "06:30 - 23:30，只於跑馬日服務"
}

# ---- ROUTES SEARCH ----

routeEnquiry = ""
routeEnquiryRoute = ""

# ---- 左側 (輸入查詢) ----
with col1:
    st.subheader("🔍 查詢路線")
    routeEnquiry = st.text_input("輸入要查詢的路線編號:", "1").strip()
    routeEnquiryRoute = st.text_input("輸入路線編號_總站代號+走線, e.g. 1_MAF1", "1_MAF1").strip().upper()  # 確保大寫

# ---- 右側 (顯示結果) ----
with col2:
    st.subheader("📌 查詢結果")

    if routeEnquiryRoute:
        st.write(f"**方向:** {routeEnquiryRoute}")

        # 直接使用 `routeEnquiryRoute` 作為 key
        route_key = routeEnquiryRoute  # 🔥 這裡修正，不再重複加 `routeEnquiry`
        
        # 顯示車站資料
        if route_key in route_stops:
            st.subheader(f"🚏 車站列表 ({routeEnquiryRoute})")
            for stop in route_stops[route_key]:
                st.write(stop)
        else:
            st.error("⚠️ 無法找到該路線的車站資料，請檢查輸入是否正確。")

        # 顯示收費資訊
        if route_key in route_fare:
            st.subheader("💰 車費資訊")
            for fare in route_fare[route_key]:
                st.write(fare)
        else:
            st.error("⚠️ 找不到該路線的收費資訊，請檢查輸入。")

        # 顯示服務時間
        if route_key in route_service_time:
            st.subheader("⏰ 服務時間")
            st.write(f"{route_service_time[route_key]}")
        else:
            st.error("⚠️ 無法找到該路線的服務時間，請檢查輸入是否正確。")

    else:
        st.warning("請輸入正確的路線編號和總站代號。")