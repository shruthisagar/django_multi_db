from alpha.models import UserData
from django.forms.models import model_to_dict


def get_latest_data():
    data = UserData.objects.only("name").last()
    data = model_to_dict(data)
    return data
def store_latest_data(name):
    UserData(
        name=name
    ).save()
    return {"status": 1}