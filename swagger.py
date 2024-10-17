import requests

def get_endpoints(swagger_url):
    response = requests.get(swagger_url)
    if response.status_code == 200:
        swagger_data = response.json()
        endpoints = swagger_data.get('paths', {}).keys()
        return list(endpoints)
    else:
        print(f"Failed to fetch Swagger JSON: {response.status_code}")
        return []

swagger_url = "http://petstore.swagger.io/v2/swagger.json"
endpoints = get_endpoints(swagger_url)

print("API Endpoints:")
for endpoint in endpoints:
    print(endpoint)

