from pymongo import MongoClient
import streamlit as st
import pandas as pd
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"] 
collection = db["drivers"] 
location = db["location"]   
proportion = db["numbox"]   
route = db['route']
car = db["car"]

citys = [c["縣市"] for c in location.find({}, {"_id": 0, "縣市": 1})]

if "page" not in st.session_state:
    st.session_state.page = None
if "form_state" not in st.session_state:
    st.session_state.form_state = {"add": False,"update": False,"delete": False}
    
c1, c2 ,c3 ,c4 ,c5 = st.columns([0.5, 0.5,0.5,0.5,0.5])
with c1:
    if (st.button("司機資料")):
        st.session_state.page = "drivers"
with c2:
    if (st.button("地點資料")):
        st.session_state.page = "locations"
with c3:
    if (st.button("比例資料")):
        st.session_state.page = "proportions"
with c4:
    if(st.button("路線資料")):
        st.session_state.page = "routes"
with c5:
    if(st.button("車輛資料")):
        st.session_state.page = "cars"

if st.session_state.page =="drivers":
    data = []
    for i in collection.find():
        data.append({"司機": i["司機"]})
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1 , col2 ,col3= st.columns([0.3,0.3,0.3])
    with col1:
        if (st.button("新增司機")):
            st.session_state.form_state = {"add": True,"update": False,"delete": False}
    with col3:
        if (st.button("刪除司機")):
            st.session_state.form_state = {"add": False,"update": False,"delete": True}
    if st.session_state.form_state["add"]:
        with st.form("add_driver_form"):
            input_name = st.text_input("輸入新增司機的名字")
            input_car = 'none'
            input_car_capability ='100'
            submitted = st.form_submit_button("確認新增")
            if submitted:
                collection.insert_one({
                    "司機": input_name,
                    "車牌": input_car,
                    "車容量": int(input_car_capability)
                })
                st.success("已新增司機！")
                st.session_state.form_state["add"] = False
                st.rerun()
    if st.session_state.form_state["update"]:
        with st.form("update_driver_form"):
            col1, col2, col3 = st.columns([0.3,0.3,0.3])
            with col1:
                input_name = st.text_input("輸入想要更新司機的名字")
            with col2:
                to_update = st.selectbox("選擇更新資料(車牌或車容量)",["司機","車牌","車容量"],key = "to_update")
            with col3:
                update_value = st.text_input(f"輸入{st.session_state.to_update}",key = "to_update_value")
            submitted = st.form_submit_button("確認更新")
            if (submitted):
                value = st.session_state.to_update_value
                if st.session_state.to_update =="車容量":
                    value = int(value)
                collection.update_one({"司機":input_name},{"$set":{st.session_state.to_update:value}})
                st.session_state.form_state["update"]=False
                st.rerun()
    if st.session_state.form_state["delete"]:
        input_name = st.text_input("輸入想要刪除司機的名字")
        submitted = st.button("確認刪除")
        if (submitted):
            collection.delete_one({"司機":input_name})
            st.session_state.form_state["delete"]=False
            st.rerun()
elif st.session_state.page =="locations":
    data = []
    for i in location.find():
        data.append({"縣市": i["縣市"], "地點": i["地點"]})
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1 , col2 = st.columns([0.5,0.5])
    with col1:
        if (st.button("新增地點")):
            st.session_state.form_state = {"add": True,"update": False,"delete": False}
    with col2:
        if (st.button("刪除地點")):
            st.session_state.form_state = {"add": False,"update": False,"delete": True}
    if st.session_state.form_state["add"]:
        with st.form("update_location_form"):
            col1, col2,  = st.columns([0.5,0.5])
            with col1:
                input_city = st.selectbox("選擇縣市",citys,key = "selectcity")
            with col2:
                input_name = st.text_input("輸入地名",key = "new_name")
            submitted = st.form_submit_button("確認新增")
            if (submitted):
                location.update_one({"縣市":st.session_state.selectcity},{"$addToSet":{"地點":st.session_state.new_name}})
                st.session_state.form_state["add"]=False
                st.rerun()
    
    if st.session_state.form_state["delete"]:
         with st.form("delete_location_form"):
            col1, col2,  = st.columns([0.5,0.5])
            with col1:
                input_city = st.selectbox("選擇縣市",citys,key = "selectcity")
            with col2:
                input_name = st.text_input("輸入地名",key = "new_name")
            submitted = st.form_submit_button("確認刪除")
            if (submitted):
                location.update_one({"縣市":st.session_state.selectcity},{"$pull":{"地點":st.session_state.new_name}})
                st.session_state.form_state["delete"]=False
                st.rerun()
elif st.session_state.page =="proportions":
    data = []
    for i in proportion.find():
        data.append({"比例": i["比例"], "箱數": i["箱數"]})
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1 , col2 ,col3= st.columns([0.3,0.3,0.3])
    with col1:
        if (st.button("新增比例")):
            st.session_state.form_state = {"add": True,"update": False,"delete": False}
    with col2:
        if (st.button("更新比例資料")):
            st.session_state.form_state = {"add": False,"update": True,"delete": False}
    with col3:
        if (st.button("刪除比例")):
            st.session_state.form_state = {"add": False,"update": False,"delete": True}
    if st.session_state.form_state["add"]:
        with st.form("add_proportion_form"):
            col1, col2 = st.columns([0.3,0.3])
            with col1:
                input_newp = st.text_input("輸入新比例",key = "new_proportion")
            with col2:
                input_newbox = st.text_input("輸入箱數",key = "new_box")
            submitted = st.form_submit_button("確認新增")
            if submitted:
                proportion.insert_one({
                    "比例": st.session_state.new_proportion,
                    "箱數": int(st.session_state.new_box),
                })
                st.success("已新增比例")
                st.session_state.form_state["add"] = False  
                st.rerun()

    if st.session_state.form_state["update"]:
        with st.form("update_proportion_form"):
            col1, col2, col3 = st.columns([0.3,0.3,0.3])
            with col1:
                input_newp = st.text_input("輸入想要更新的比例",key = "new_proportion")
            with col2:
                to_update = st.selectbox("選擇更新資料(比例或箱數)",["比例","箱數"],key = "to_update")
            with col3:
                update_value = st.text_input(f"輸入{st.session_state.to_update}",key = "to_update_value")
            submitted = st.form_submit_button("確認更新")
            if (submitted):
                value = st.session_state.to_update_value
                if st.session_state.to_update =="箱數":
                    value = int(value)
                proportion.update_one({"比例":st.session_state.new_proportion},{"$set":{st.session_state.to_update:value}})
                st.session_state.form_state["update"]=False
                st.rerun()
    if st.session_state.form_state["delete"]:
        input_name = st.text_input("輸入想要刪的比例")
        submitted = st.button("確認刪除")
        if (submitted):
            proportion.delete_one({"比例":input_name})
            st.session_state.form_state["delete"]=False
            st.rerun()
elif st.session_state.page == "routes":

    data = []
    for r in route.find():
        data.append({
            "路線": r["路線"],
            "地點": "、".join(r["地點"])  
        })
    st.dataframe(pd.DataFrame(data), use_container_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("新增路線"):
            st.session_state.form_state = {"add": True, "update": False, "delete": False}
    with col2:
        if st.button("更新路線"):
            st.session_state.form_state = {"add": False, "update": True, "delete": False}
    with col3:
        if st.button("刪除路線"):
            st.session_state.form_state = {"add": False, "update": False, "delete": True}

    if st.session_state.form_state["add"]:
        with st.form("add_route_form"):
            route_name = st.text_input("輸入路線名稱", key="new_route")
            route_places = st.text_input("輸入地點（用逗號分隔）", key="new_places")
            submitted = st.form_submit_button("確認新增")

            if submitted:
                places = [p.strip() for p in route_places.split(",") if p.strip()]
                route.insert_one({"路線": route_name, "地點": places})
                st.session_state.form_state["add"] = False
                st.rerun()

    if st.session_state.form_state["delete"]:
        with st.form("delete_route_form"):
            all_routes = [r["路線"] for r in route.find()]
            selected = st.selectbox("選擇要刪除的路線", all_routes, key="del_route")
            submitted = st.form_submit_button("確認刪除")

            if submitted:
                route.delete_one({"路線": selected})
                st.session_state.form_state["delete"] = False
                st.rerun()

    if st.session_state.form_state["update"]:
        all_routes = [r["路線"] for r in route.find()]
        selected_route = st.selectbox("選擇路線", all_routes, key="upd_route")

        action = st.radio("選擇操作", ["新增地點", "刪除地點"])

        if action == "新增地點":
            new_place = st.text_input("輸入新地點", key="add_place")
        elif action =='刪除地點':
            places = route.find_one({"路線": st.session_state.upd_route})['地點']
            del_place = st.selectbox("選擇要刪除的地點", places, key="del_place_item")
        if st.button("確認更新"):
            if action == "新增地點":
                route.update_one(
                    {"路線": selected_route},
                    {"$addToSet" : {"地點": st.session_state.add_place}}
                )
            else:
                route.update_one(
                    {"路線": selected_route},
                    {"$pull": {"地點": st.session_state.del_place_item}}
                )

            st.session_state.form_state["update"] = False
            st.rerun()
elif st.session_state.page == "cars":
    data = []
    for i in car.find():
        data.append({"車牌": i["車牌"], "車容量": i["車容量"]})
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("新增車輛"):
            st.session_state.form_state = {"add": True, "update": False, "delete": False}
    with col2:
        if st.button("刪除車輛"):
            st.session_state.form_state = {"add": False, "update": False, "delete": True}
    if st.session_state.form_state["add"]:
        with st.form("add_car_form"):
            car_name = st.text_input("輸入車牌", key="new_car")
            car_capability = int(st.number_input("輸入車容量(箱數)", key="new_capability",step = 1,format ='%d'))
            submitted = st.form_submit_button("確認新增")

            if submitted:
                car.insert_one({"車牌": car_name, "車容量": car_capability})
                st.session_state.form_state["add"] = False
                st.rerun()
    if st.session_state.form_state["delete"]:
        with st.form("delete_car_form"):
            all_cars = [r["車牌"] for r in car.find()]
            selected = st.selectbox("選擇要刪除的車牌", all_cars, key="del_car")
            submitted = st.form_submit_button("確認刪除")
            if submitted:
                car.delete_one({"車牌": selected})
                st.session_state.form_state["delete"] = False
                st.rerun()
        