Feature: Event Availability
  User can create his/her availability for a specific event
  Scenario: Adding Availability
    Given User have created an event
    When User adds a "2022-11-24-9-00" to event
    Then Selected date-times are added to user's event
