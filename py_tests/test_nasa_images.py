import pytest
from API.view.images_view import custom_assert_json
from API.NasaAPI import NasaAPI


@pytest.mark.NasaImages
def test_images():
    images = NasaAPI()
    images_by_sol = images.querying_photos_by_sol(1000)
    images_eath_date = images_by_sol['photos'][0]['earth_date']
    images_by_earth_date = images.querying_photos_by_earth_date(images_eath_date)
    custom_assert_json(images_by_sol, images_by_earth_date)
