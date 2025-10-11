import requests

# 요청을 보낼 URL
url = "http://localhost:9880/parse.test"

# 전송할 JSON 데이터
data_list = [
    {"@timestamp":"2025-07-09","message":"BOAN_Master","source.ip":"198.55.98.201","destination.ip":"61.110.14.40","event.kind":"traffic","event.category":"forward"}
    , {"@timestamp":"2025-07-09","message":"BOAN_Master","source.ip":"203.240.129.209","destination.ip":"58.180.85.66","event.kind":"traffic","event.category":"local"}
]

# 순서대로 요청
for data in data_list:
    response = requests.post(url, json=data, timeout=10)
    print("요청 데이터:", data)
    print("응답 코드:", response.status_code)
    print("응답 내용:", response.text)
    print("="*40)
