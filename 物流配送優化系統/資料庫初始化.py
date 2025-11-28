from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]#database
#司機
collection = db["drivers"]
data = {"司機":'呂維崧',"車牌":'aaa',"車容量":290}
collection.insert_one(data)
data = {"司機":'葉烸平',"車牌":'aaa',"車容量":290}
collection.insert_one(data)

#地點
location = db["location"]
data = {"縣市":"嘉義","地點":['和平','頭橋','民雄','朴子']}
location.insert_one(data)
data = {"縣市":"台南","地點":['鹽水','中華','開元','五王','灣里','大同','建平','仁德','富農','東安','西港','佳里','學甲','崇德','金華','健康','育德']}
location.insert_one(data)
data = {"縣市":"高雄","地點":['楠梓','九如','覺民','二苓','岡山','彌陀','藍田','寶珠溝','三民','華寧','鳳松','大寮','瑞北']}
location.insert_one(data)
data = {"縣市":"屏東","地點":['九如','廣東','大武','里港','內埔','潮州']}
location.insert_one(data)

#比例
proportion = db["numbox"]
data = {"比例":"12","箱數":30}
proportion.insert_one(data)
data = {"比例":"18","箱數":55}
proportion.insert_one(data)
data = {"比例":"24","箱數":70}
proportion.insert_one(data)
data = {"比例":"30","箱數":85}
proportion.insert_one(data)
data = {"比例":"36","箱數":95}
proportion.insert_one(data)
data = {"比例":"42","箱數":120}
proportion.insert_one(data)




#路線
route = db["route"]
data = {"路線":"大武線","地點":['九如','廣東','大武']}
route.insert_one(data)
data = {"路線":"潮州線","地點":['里港','內埔','潮州']}
route.insert_one(data)
data = {"路線":"三民線","地點":['寶珠溝','三民','華寧']}
route.insert_one(data)
data = {"路線":"岡山線","地點":['岡山','彌陀','藍田']}
route.insert_one(data)
data = {"路線":"大寮線","地點":['鳳松','大寮','瑞北']}
route.insert_one(data)
data = {"路線":"仁德線","地點":['仁德','富農','東安']}
route.insert_one(data)
data = {"路線":"大同線","地點":['灣里','大同','建平']}
route.insert_one(data)
data = {"路線":"中華線","地點":['中華','開元','五王']}
route.insert_one(data)
data = {"路線":"鹽水線","地點":['鹽水','朴子','麻魚寮']}
route.insert_one(data)
data = {"路線":"民雄線","地點":['和平','頭橋','民雄']}
route.insert_one(data)

car = db["car"]
data = {"車牌":'車輛1',"車容量":290}
car.insert_one(data)
data = {"車牌":'車輛2',"車容量":250}
car.insert_one(data)
data = {"車牌":'車輛3',"車容量":240}
car.insert_one(data)
data = {"車牌":'車輛4',"車容量":230}
car.insert_one(data)
data = {"車牌":'車輛5',"車容量":220}
car.insert_one(data)
data = {"車牌":'車輛6',"車容量":260}
car.insert_one(data)
