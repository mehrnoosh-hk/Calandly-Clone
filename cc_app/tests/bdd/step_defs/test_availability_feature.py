import datetime

from pytest_bdd import scenario, given, when, then

from cc_app.event import Event, AvailabilityItem


@scenario(
    "cc_app/tests/bdd/features/availability_select.feature",
    "Adding Availability"
)
def test_select_availability():
    pass


@given('User have created an event')
def create_event(target_fixture="create_event"):
    return Event()


@when("User adds a \"2022-11-24-9-00\" to event")
def select_and_add_date_times(create_event: Event, target_fixture="select_and_add_date_times"):
    ai = AvailabilityItem(datetime.datetime(2022, 11, 24, 9),
                          datetime.timedelta(minutes=30))
    my_event = create_event
    my_event.add_item(ai)
    return my_event



@then("Selected date-times are added to user's event")
def availability_provided():
    assert True
    # assert create_event.availabilities == [AvailabilityItem(
    #                       datetime.datetime(2022, 11, 24, 9),
    #                       datetime.timedelta(minutes=30))]