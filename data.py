class TestData:

    #Тестовые наборы данных для проверки создания поста:
    #1.Набор валидных данных
    cteate_post_positive={
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }

    #2.Набор с пустым Json
    create_post_missing_json = {}

    #3. Набор с отсутствующей строкой title
    create_post_invalid_missing_title = {
        "body": 'bar',
        "userId": 1
    }

    #4. Набор с отсутствующей строкой body
    create_post_invalid_missing_body = {
        "title": 'foo',
        "userId": 1
    }

    #5. Набор с отсутствующей строкой userId
    create_post_invalid_missing_userId = {
        "title": 'foo',
        "body": 'bar'
    }

    #6. Набор с числовым форматом в title
    create_post_int_title ={
        "title": 1,
        "body": 'bar',
        "userId": 1
    }

    # 7. Набор с числовым форматом в body
    create_post_int_body = {
        "title": 'foo',
        "body": 1,
        "userId": 1
    }

    #8. Набор со строковым форматом в userId
    create_post_str_userId = {
        "title": 'foo',
        "body": 'bar',
        "userId": '1'
    }

    # 9. Набор с булевым значением в title
    create_post_bool_title = {
        "title": True,
        "body": 'bar',
        "userId": 1
    }

    #10. Набор с булевым значением в body
    create_post_bool_body = {
        "title": 'foo',
        "body": True,
        "userId": 1
    }

    #11. Набор с булевым значением в userId
    create_post_bool_userId = {
        "title": 'foo',
        "body": 'bar',
        "userId": True
    }

    #12. Набор со значением null в title
    create_post_null_title = {
        "title": None,
        "body": 'bar',
        "userId": 1
    }

    #13. Набор со значением null в body
    create_post_null_body = {
        "title": 'foo',
        "body": None,
        "userId": 1
    }

    #14. Набор со значением null в userId
    create_post_null_userId = {
        "title": 'foo',
        "body": 'bar',
        "userId": None
    }

    #15. Набор с несуществующим id в userId
    create_post_invalid_userId = {
        "title": 'foo',
        "body": 'bar',
        "userId": -1
    }

    # Тестовые наборы данных для проверки обновления поста:
    # 1.Набор валидных данных
    update_post_positive = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }

    #2. Набор с пустым Json
    update_post_invalid_json = {}


    #3. Набор с отсутствующим id
    update_post_missing_id = {
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }


    #4. Набор с отсутствующим title
    update_post_missing_title = {
        "id": 1,
        "body": 'bar',
        "userId": 1
    }

    #5. Набор с отсутствующим body
    update_post_missing_body = {
        "id": 1,
        "title": 'foo',
        "userId": 1}


    #6. Набор с отсутствующим userId
    update_post_missing_userId = {
        "id": 1,
        "title": 'foo',
        "body": 'bar'
    }

    #7. Набор со строковым форматом id
    update_post_str_id = {
        "id": '1',
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }

    #8. Набор со строковым форматом userId
    update_post_str_userId = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": '1'
    }

    #9. Набор с числовым форматом title
    update_post_int_title = {
        "id": 1,
        "title": 1,
        "body": 'bar',
        "userId": 1
    }

    #10. Набор с числовым форматом body
    update_post_int_body = {
        "id": 1,
        "title": 'foo',
        "body": 1,
        "userId": 1
    }

    #11. Набор с булевым значением id
    update_post_bool_id = {
        "id": True,
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }

    #12. Набор с булевым значением title
    update_post_bool_title = {
        "id": 1,
        "title": True,
        "body": 'bar',
        "userId": 1
    }

    #13. Набор с булевым значением body
    update_post_bool_body = {
        "id": 1,
        "title": 'foo',
        "body": True,
        "userId": 1
    }

    #14. Набор с булевым значением userId
    update_post_bool_userId = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": True
    }

    #15. Набор со значением null в id
    update_post_null_id = {
        "id": None,
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }

    #16. Набор со значением null в title
    update_post_null_title = {
        "id": 1,
        "title": None,
        "body": 'bar',
        "userId": 1
    }

    #17. Набор со значением null в body
    update_post_null_body = {
        "id": 1,
        "title": 'foo',
        "body": None,
        "userId": 1
    }

    #18. Набор со значением null в userId
    update_post_null_userId = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": None
    }

    #19. Набор с несуществющим id
    update_post_invalid_userId = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": -1
    }

    #20. Набор с несуществующим userId
    update_post_invalid_id = {
        "id": -1,
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }
    #Статус коды ответов:
    CREATE_OK = 201
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404