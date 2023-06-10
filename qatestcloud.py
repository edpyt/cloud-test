import requests

API_URL = 'https://jsonplaceholder.typicode.com/'

REQUEST_POST_URL = API_URL + 'posts/'
EXPECTED_COLUMNS = ('userId', 'id', 'title', 'body') 
EXPECTED_TYPES = (int, int, str, str)
    

def test_get_posts():
    response = requests.get(REQUEST_POST_URL)        
    
    assert response.status_code == 200
            
    response_data = response.json()
    
    assert len(response_data) == 100  # вместо конкретного числа количество
                                      # строк в таблице
    # проверка столбцов
    assert all(tuple(user.keys()) == EXPECTED_COLUMNS
               for user in response_data)
    # проверка данных в столбцах
    assert all(tuple(map(type, user.values())) == EXPECTED_TYPES
                for user in response_data)
    
    
def test_get_post_from_posts():
    response = requests.get(REQUEST_POST_URL + '100')
    response_data =response.json()
    test_data = {'userId': 10, 'id': 100, 'title': 'at nam consequatur ea labore ea harum',
                 'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut'}
    
    assert response.status_code == 200
    assert response_data == test_data
    assert tuple(response_data.keys()) == EXPECTED_COLUMNS
    assert tuple(map(type, response_data.values())) == EXPECTED_TYPES


def test_get_post_from_posts_wrong():
    response = requests.get(REQUEST_POST_URL + '100')
    response_data = response.json()
    test_data = {'userId': 10, 'id': 100, 'title': 'at nam consequatur ea labore ea harum',
                'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut'}


    assert response.status_code == 200
    assert response_data == test_data
    assert tuple(response_data.keys()) == EXPECTED_COLUMNS
    assert tuple(map(type, response_data.values())) == EXPECTED_TYPES
    



def test_post_posts():
    test_data = {
        'userId': 11,
        'id': 101,
        'title': 'lorum ipsum',
        'body': 'yes, lorum ipsum'
    }
    response = requests.post(REQUEST_POST_URL, test_data)
    response_data = response.json()
    
    assert response.status_code == 201
    assert tuple(response_data.keys()) == EXPECTED_COLUMNS
    assert tuple(map(type, response_data.values())) != EXPECTED_TYPES
    

def test_posts_posts_wrong():
    test_data = {
        'userId': 'ahahhaha',
        'id': 'Omeds',
        'title': 1,
        'body': 5
    }
    
    response = requests.post(REQUEST_POST_URL, test_data)
    
    response_data = response.json()
    
    assert response.status_code == 201
    assert tuple(response_data.keys()) == EXPECTED_COLUMNS
    assert tuple(map(type, response_data.values())) != EXPECTED_TYPES


def test_delete_from_posts():
    response = requests.delete(REQUEST_POST_URL + '101')
    
    assert response.status_code == 200
   
    response_get_data = requests.get(REQUEST_POST_URL).json()
    assert len(response_get_data) == 100
 
 
def test_delete_from_posts_wrong():  
    response = requests.delete(REQUEST_POST_URL + '1337')
    
    assert response.status_code == 200
    assert response.json() == {}
