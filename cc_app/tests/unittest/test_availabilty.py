import datetime
import pytest
from cc_app.event import Event, AvailabilityItem


def test_create_and_initialize_event():
    ma = Event()
    assert ma.availabilities is not None
    assert ma.availabilities == []


def test_initializing_availability_item_default_values():
    ai = AvailabilityItem()
    assert isinstance(ai.start, datetime.datetime)
    assert isinstance(ai.duration, datetime.timedelta)


def test_initializing_availability_item_with_values():
    start = datetime.datetime.now()
    ai = AvailabilityItem(start=start, duration=datetime.timedelta(minutes=5))
    assert ai.start + ai.duration == start + datetime.timedelta(minutes=5)


def test_initializing_availability_item_with_wrong_values():
    start = "START"
    duration = "DURATION"
    with pytest.raises(TypeError) as te:
        ai = AvailabilityItem(start, duration)
    assert te.value.args[0] == "Expecting Date-Time"

    with pytest.raises(ValueError) as ve:
        ai = AvailabilityItem(datetime.datetime.now(), datetime.timedelta(
            minutes=-2))
    assert ve.value.args[0] == "Duration should be positive"

def test_adding_availability_item_to_event(list_of_availability_items):
    list_of_availabilities = list_of_availability_items
    my_availability = Event()
    for ai in list_of_availabilities:
        my_availability.add_item(ai)
    assert my_availability.availabilities != []


def test_retrieve_availabilities_for_event():
    e = Event()
    ai = AvailabilityItem(
        start=datetime.datetime(2022, 11, 7, 11, 30),
        duration=datetime.timedelta(minutes=30)
    )
    e.add_item(ai)
    assert e.availabilities[0] is ai
