import requests
import json

city = "Paris"
apikey = "7450b2a28a0c0341fe8a895da0a53532"
lang="kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
print(api)

result = requests.get(api)

data = json.loads(result.text)

#print(type(result.text))
#print(type(data))

print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("===================================")
print("현재 온도는", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은", data["main"]["temp_min"], "입니다.")
print("최고 기온은", data["main"]["temp_max"], "입니다.")
print("===================================")
print("기압은",data["main"]["pressure"], "입니다.")
print("습도는",data["main"]["humidity"], "입니다.")
print("===================================")
print("가시거리는",data["visibility"],"입니다.")
print("풍속은",data["wind"]["speed"], "입니다.")
print("풍향은",data["wind"]["deg"], "입니다.")
print("구름은",data["clouds"]["all"],"입니다.")
print("===================================")
print("일출은",data["sys"]["sunrise"],"입니다.")
print("일몰은",data["sys"]["sunset"], "입니다.")


