import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        user = config.get('common info', 'useremail')
        return user

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password