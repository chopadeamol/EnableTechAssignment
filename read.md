To run the tests in parallel:
python -m pytest -n=4 --html=reports\report\chrome.html --browser chrome

To run the tests sequentially:
python -m pytest --html=reports\report\chrome.html --browser chrome

To view allure report, hit the following command in your project directory path:
allure serve allure-results

To generate allure report:
python -m pytest --alluredir="D:\EnableTechnologiesTest\allure-results" test_cases/test_login.py --browser chrome  




