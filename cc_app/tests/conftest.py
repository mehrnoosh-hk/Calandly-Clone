from pytest import fixture
from cc_app.event import AvailabilityItem, Event
import datetime


@fixture()
def list_of_availability_items():
    ai_1 = AvailabilityItem(
        start=datetime.datetime(2022, 11, 24, 8, 15),
        duration=datetime.timedelta(minutes=15)
    )
    ai_2 = AvailabilityItem(
        start=datetime.datetime(2022, 11, 5, 12, 15),
        duration=datetime.timedelta(minutes=15)
    )
    ai_3 = AvailabilityItem(
        start=datetime.datetime(2022, 11, 24, 8, 15),
        duration=datetime.timedelta(minutes=15)
    )
    return [ai_1, ai_2, ai_3]


@fixture()
def event_with_availability(list_of_availability_items):
    e = Event()
    ai_list = list_of_availability_items
    for ai in ai_list:
        e.add_item(ai)
    return e
