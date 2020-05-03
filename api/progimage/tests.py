import pytest
import base64

from io import BytesIO
from PIL import Image as img

from .models import Image


@pytest.fixture
def image_base64():
    file = BytesIO()
    image = img.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return base64.b64encode(file.read()).decode('utf-8')


@pytest.mark.django_db
def test_image(client, image_base64):
    response = client.post(
        '/progimage/images/',
        {'image': image_base64},
        format='json'
    )
    
    assert response.status_code == 201
    assert Image.objects.count() == 1
    
    response_data = response.json()
    assert 'id' in response_data.keys()

    id = response_data['id']
    response = client.get(
        f'/progimage/images/{id}/'
    )

    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data['id'] == id
