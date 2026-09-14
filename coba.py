import json

data = {
    "nama": "Andi",
    "umur": 20,
    "hobi": ["coding", "membaca"]
}

json_str = json.dumps(data)
print("JSON:", json_str)

obj = json.loads(json_str)
print("Nama:", obj["nama"])