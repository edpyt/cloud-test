import requests


class TestCloud:
    API_URL = 'https://jsonplaceholder.typicode.com/'
    
    def __init__(self):
        self.request_posts_url = self.API_URL + 'posts'
        self.expected_columns = ('userId', 'id', 'title', 'body') 
    
    # Проверка столбцов
    def values_in_dict(self, u_dict):
        for u_data in self.expected_columns:
            if u_data not in u_dict:
                return False
        return True
    
    def test_get_posts(self):
        response = requests.get(self.request_posts_url)        
        
        assert response.status_code == 200
                
        response_data = response.json()

        assert len(response_data) == 100
        assert all(self.values_in_dict(user) for user in response_data)

    def test_post_posts(self):
        test_data = {'userId': 11, 'id': 101,
                     'title': 'lorum ipsum',
                     'body': 'yes, lorum ipsum'}
        response = requests.post(self.request_posts_url, test_data)
        
        assert response.status_code == 201
        
        # Тест неправильно введёных данных
        test_data = {'userId': 'ahahhaha', 'id': 'Omeds',
                        'title': 1,
                        'body': 5}
            
        response = requests.post(self.request_posts_url, test_data)
        
        response_data = response.json()
        
        assert response.status_code == 201
        assert isinstance(response_data['body'], str)
        assert isinstance(response_data['title'], str)

    def test_delete_from_posts(self):
        response = requests.delete(self.request_posts_url)

        response_data = response.json()
        
        assert response.status_code == 404  # 0_0
        assert len(response_data) == 0        
        
        
if __name__ == '__main__':
    x = TestCloud()
    x.test_get_posts()
    x.test_post_posts()
    x.test_delete_from_posts()
    print('Тесты выполнены успешно!')