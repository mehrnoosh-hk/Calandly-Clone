import datetime


class AvailabilityItem:
    def __init__(self, start: datetime.datetime = datetime.datetime.now(),
                 duration: datetime.timedelta = datetime.timedelta(
                     minutes=15)):
        check_types = [
            isinstance(start, datetime.datetime),
            isinstance(duration, datetime.timedelta),
        ]
        if not all(check_types):
            raise TypeError("Expecting Date-Time")

        check_values = [
            duration > datetime.timedelta()
        ]

        if not all(check_values):
            raise ValueError("Duration should be positive")

        self.start = start
        self.duration = duration


class Event:
    def __init__(self):
        self.availabilities = []

    def add_item(self, availability_item: AvailabilityItem):
        if not isinstance(availability_item, AvailabilityItem):
            raise TypeError
        self.availabilities.append(availability_item)
