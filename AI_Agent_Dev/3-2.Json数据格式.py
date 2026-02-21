import json

d = {
    "name": "Bob",
    "age": 11,
    "gender": "男"
}

# json.dumps(字典或列表,ensure_ascii=False)：将字典或列表 转换为 Json字符串
# ensure_ascii：参数确保中文能正常显示
s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
        "name": "Bob",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "Amy",
        "age": 15,
        "gender": "女"
    },
    {
        "name": "David",
        "age": 17,
        "gender": "男"
    }
]

# json.loads(json字符串)：将Json字符串 转换为 Python字典或列表
m = json.dumps(l, ensure_ascii=False)
print(m)

json_str = '{"name": "Bob", "age": 11, "gender": "男"}'
json_array_str = '[{"name": "Bob", "age": 11, "gender": "男"}, {"name": "Amy", "age": 15, "gender": "女"}, {"name": "Daivd", "age": 17, "gender": "男"}]'


res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))

