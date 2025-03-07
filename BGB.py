import streamlit as st

#emoji sources: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="漢堡巴士路線資料", page_icon=":Oncoming Bus:", layout="wide")

# ---- HEADER SECTIONS ----

with st.container():
    st.title("漢堡巴士路線")
    st.subheader("可在此查閱漢堡巴士各路線的詳細資料及其轉乘優惠。")
    st.write("[可參考 >](https://docs.google.com/spreadsheets/d/1_hF_4ObI7j7OKKa__Bs9-fCLS6jYLvtTxg_nzhzkLjU/edit?gid=956048970#gid=956048970)")

# ---- ROUTES DETAILS ----

#路線方向
route_directions = {
    "1": ["MAF1", "MAF2", "HVU1", "HVU2", "HVU3"]}

#車站資料
route_stops = {
    "MAF1": ["1.跑馬地 (上)，蟠龍道", "2.箕鏈坊，藍塘道", "3.桂芳街，成和道", "4.山村道，成和道", "5.景光街",
             "6.養和醫院，黃泥涌道", "7.跑馬地馬場，黃泥涌道", "8.立德里，摩利臣山道", "9.利景酒店，灣仔道",
             "10.普樂里，灣仔道", "11.修頓球場，軒尼詩道", "12.晏頓街，軒尼詩道", "13.金鐘 - 太古廣場，金鐘道",
             "14.中銀大廈，金鐘道", "15.置地廣場，德輔道中", "16.中環街市，德輔道中", "17.急庇利街，德輔道中",
             "18.上環 - 港澳碼頭"],

    "MAF2": ["1.跑馬地 (上)，蟠龍道", "2.箕鏈坊，藍塘道", "3.桂芳街，成和道", "4.山村道，成和道", "5.景光街",
             "6.養和醫院，黃泥涌道", "7.立德里，摩利臣山道", "8.利景酒店，灣仔道", "9.普樂里，灣仔道",
             "10.修頓球場，軒尼詩道", "11.晏頓街，軒尼詩道", "12.金鐘 - 太古廣場，金鐘道",
             "13.中銀大廈，金鐘道", "14.置地廣場，德輔道中", "15.中環街市，德輔道中", "16.急庇利街，德輔道中",
             "17.上環 - 港澳碼頭"]
             }

#服務時間
route_service_time = {
    "MAF1": "06:00 - 23:00",
    "MAF2": "06:30 - 23:30"
}

# ---- ROUTES SEARCH ----

routeEnquiry = " "
routeEnquiryRoute = " "

with st.container():
    st.title("路線查詢")

    routeEnquiry = st.text_input("輸入要查詢的路線編號:", "1")
    routeEnquiryRoute = st.text_input("總站代號+走線, e.g. MAF1", "MAF1")

    if routeEnquiry and routeEnquiryRoute:
        if routeEnquiry in route_directions:
            directions = route_directions[routeEnquiry]

            # 確保查詢的走線在可選方向內
            if routeEnquiryRoute in directions:
                st.subheader(f"路線方向: {routeEnquiryRoute}")
                st.write(f"可選擇的方向: {', '.join(directions)}")

                # 顯示車站資訊
                if routeEnquiryRoute in route_stops:
                    st.subheader(f"車站列表 ({routeEnquiryRoute})")
                    for stop in route_stops[routeEnquiryRoute]:
                        st.write(stop)
                else:
                    st.error("無法找到該路線的車站資料，請檢查輸入是否正確。")

                # 顯示服務時間
                if routeEnquiryRoute in route_service_time:
                    st.subheader("服務時間")
                    st.write(f"{route_service_time[routeEnquiryRoute]}")
                else:
                    st.error("無法找到該路線的服務時間，請檢查輸入是否正確。")

            else:
                st.error("無效的方向選項，請輸入正確的總站代號+走線。")
        else:
            st.error("找不到該路線的方向資訊，請確認輸入是否正確。")