import requests

url_cs = "https://openapi.data.uwaterloo.ca/v3/Courses/1239/cs"
url_math = "https://openapi.data.uwaterloo.ca/v3/Courses/1239/math"
url_stat = "https://openapi.data.uwaterloo.ca/v3/Courses/1239/stat"
headers = {'x-api-key': 'B4AFD97679334F848DBAFF54C5A44160'}

list_cs = requests.get(url_cs, headers=headers).json()
list_math = requests.get(url_math, headers=headers).json()
list_stat = requests.get(url_stat, headers=headers).json()

print(len(list_cs), len(list_math), len(list_stat))

course_dict = {}
course_dict["cs"] = [x["catalogNumber"] for x in list_cs]
course_dict["math"] = [x["catalogNumber"] for x in list_math]
course_dict["stat"] = [x["catalogNumber"] for x in list_stat]
print(course_dict)