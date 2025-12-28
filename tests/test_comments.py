from data import TestData
from urls import TestEndpoint

import allure


class TestComments:

    @allure.title('Успешное получение списка комментариев к посту')
    def test_get_comments(self,session):
        response = session.get(TestEndpoint.url_get_comments)
        assert (response.status_code == TestData.OK and isinstance(response.json(), list)
                and len(response.json())>0)

        for comment in response.json():
            assert ("postId" in comment and "id" in comment and "name" in comment
                    and "email" in comment and "body" in comment)


    @allure.title('Проверка получения списка комментариев к посту с несущестующим id поста')
    def test_get_comments_with_invalid_post(self, session):
        invalid_post_id = 999999
        url_with_invalid_post = TestEndpoint.url_update.replace('1', str(invalid_post_id))

        response = session.get(url_with_invalid_post)
        assert response.status_code == TestData.NOT_FOUND


