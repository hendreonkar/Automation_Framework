import pytest
import allure
import requests

@allure.title("Test GET request- Restful booker")
@allure.description("To verify GET requests by booking ids")
@allure.tag("regression", "smoke", "P0")

@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url= "https://restful-booker.herokuapp.com/booking/2"
    responseData=requests.get(url)
    print(responseData.text)
    assert responseData.status_code==200

@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404

