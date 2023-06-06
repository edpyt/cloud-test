import requests

API_URL = 'https://jsonplaceholder.typicode.com/'

REQUEST_POST_URL = API_URL + 'posts'
EXPECTED_COLUMNS = ('userId', 'id', 'title', 'body') 
EXPECTED_TYPES = (int, int, str, str)
    
# Проверка столбцов
def values_in_dict(u_dict):
    for u_data in EXPECTED_COLUMNS:
        if u_data not in u_dict:
            return False
    return True

def test_get_posts():
    response = requests.get(REQUEST_POST_URL)        
    
    assert response.status_code == 200
            
    response_data = response.json()
    # проверка столбцов
    assert all(values_in_dict(user) for user in response_data)
    # проверка данных в столбцах
    assert all(tuple(map(type, user.values())) == EXPECTED_TYPES
                for user in response_data)
    

def test_post_posts():
    # Тест правильно введённых данных
    test_data = {'userId': 11, 'id': 101,
                    'title': 'lorum ipsum',
                    'body': 'yes, lorum ipsum'}
    response = requests.post(REQUEST_POST_URL, test_data)
    
    assert response.status_code == 201
    
    # Тест неправильно введёных данных
    test_data = {'userId': 'ahahhaha', 'id': 'Omeds',
                    'title': 1,
                    'body': 5}
        
    response = requests.post(REQUEST_POST_URL, test_data)
    
    response_data = response.json()
    
    assert response.status_code == 201
    assert isinstance(response_data['body'], str)
    assert isinstance(response_data['title'], str)

def test_delete_from_posts():
    response = requests.delete(REQUEST_POST_URL)

    response_data = response.json()
    
    assert response.status_code == 404  # 0_0
    assert len(response_data) == 0        