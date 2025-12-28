import allure
import pytest

from data import TestData
from urls import TestEndpoint


class TestPosts:

    @allure.title('Успешное создание поста')
    def test_post_create_positive(self, session):

        payload = TestData.cteate_post_positive

        response=session.post(TestEndpoint.url_create, json=payload)

        assert (response.status_code == TestData.CREATE_OK
                and response.json()["title"] == payload["title"]
                and response.json()["body"] == payload["body"]
                and response.json()["userId"] == payload["userId"])


    @allure.title('Проверка создания поста с невалидными данными')
    @pytest.mark.parametrize("payload", [TestData.create_post_invalid_missing_title,
                                         TestData.create_post_invalid_missing_body,
                                         TestData.create_post_invalid_missing_userId,
                                         TestData.create_post_int_title,
                                         TestData.create_post_int_body,
                                         TestData.create_post_str_userId,
                                         TestData.create_post_bool_title,
                                         TestData.create_post_bool_body,
                                         TestData.create_post_bool_userId,
                                         TestData.create_post_null_title,
                                         TestData.create_post_null_body,
                                         TestData.create_post_null_userId,
                                         TestData.create_post_invalid_userId,
                                         TestData.create_post_missing_json])
    def test_post_create_negative(self, session, payload):

        response = session.post(TestEndpoint.url_create, json=payload)

        assert response.status_code == TestData.BAD_REQUEST


    @allure.title('Успешное обновление поста')
    def test_post_update_positive(self, session):
        payload = TestData.update_post_positive

        response=session.put(TestEndpoint.url_update, json=payload)
        assert (response.status_code == TestData.OK
                and response.json()["id"] == payload["id"]
                and response.json()["title"] == payload["title"]
                and response.json()["body"] == payload["body"]
                and response.json()["userId"] == payload["userId"])


    @allure.title('Проверка обновления поста с невалидными данными')
    @pytest.mark.parametrize("payload",[TestData.update_post_invalid_json,
                                        TestData.update_post_missing_id,
                                        TestData.update_post_missing_body,
                                        TestData.update_post_missing_title,
                                        TestData.update_post_missing_userId,
                                        TestData.update_post_bool_body,
                                        TestData.update_post_bool_id,
                                        TestData.update_post_bool_title,
                                        TestData.update_post_bool_userId,
                                        TestData.update_post_int_body,
                                        TestData.update_post_int_title,
                                        TestData.update_post_str_id,
                                        TestData.update_post_str_userId,
                                        TestData.update_post_null_id,
                                        TestData.update_post_null_title,
                                        TestData.update_post_null_body,
                                        TestData.update_post_null_userId,
                                        TestData.update_post_invalid_id,
                                        TestData.update_post_invalid_userId])
    def test_post_update_negative(self, session, payload):
        response = session.post(TestEndpoint.url_update, json=payload)

        assert response.status_code == TestData.BAD_REQUEST


    @allure.title('Успешное удаление поста')
    def test_post_delete(self, session):
        response = session.delete(TestEndpoint.url_update)

        assert  response.status_code == TestData.OK



