import requests
from config.enviroment import *
from exception.exceptions import ExpectedStatusCodeError


class Nasa(object):
    def __init__(self):
        self.session = nasa()

    def querying_photos(self, dto):
        """
        :param dto
        :return:
        """
        return requests.get(url=self.session + '/mars-photos/api/v1/rovers/curiosity/photos', params=dto)


class NasaAPI(object):
    def __init__(self):
        self.nasa = Nasa()

    def create_querying__by_sol_dto(self, sol):
        return {
            "sol": sol,
            "api_key": api_key()
        }

    def create_querying_by_earth_date_dto(self, earth_date):
        return {
            "earth_date": earth_date,
            "api_key": api_key()
        }

    def querying_photos_by_sol(self, sol):
        request = self.nasa.querying_photos(self.create_querying__by_sol_dto(sol))
        if request.status_code != 200:
            raise ExpectedStatusCodeError(request, 200)
        return request.json()

    def querying_photos_by_earth_date(self, sol):
        request = self.nasa.querying_photos(self.create_querying_by_earth_date_dto(sol))
        if request.status_code != 200:
            raise ExpectedStatusCodeError(request, 200)
        return request.json()
