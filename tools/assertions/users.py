from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(request: UserSchema, response: UserSchema):
    """
    Проверяет, что данные пользователя соответствуют ожидаемым

    :param request: Фактические данные пользователя.
    :param response: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.id, request.id, "id")
    assert_equal(response.email, request.email, "email")
    assert_equal(response.last_name, request.last_name, "last_name")
    assert_equal(response.first_name, request.first_name, "first_name")
    assert_equal(response.middle_name, request.middle_name, "middle_name")


def assert_get_user_response(request: GetUserResponseSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что данные пользователя при создании и при запросе совпадают.

    :param request: Исходный запрос на получение данных пользователя.
    :param response: Ответ API с данными пользователя при создании.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(request.user, response.user)
