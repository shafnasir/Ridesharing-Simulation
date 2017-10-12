from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        True
        """
        # TODO
        self.avail_Driver = []
        self.waiting_List = []


    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        # TODO

        return "Drivers Available: {0}, Riders wait list: {1}".format(len(self.avail_Driver),len(self.waiting_List))

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        Too many things to be called for an example
        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None

        """
        all_DriversTimes =[]

        if self.avail_Driver:

            for driver in self.avail_Driver: # goes through the available drivers to find the fastest driver for the rider

                all_DriversTimes.append(driver.get_travel_time(rider.origin)) #adding all the driver times to a list
            Best_Driver = all_DriversTimes.index(min(all_DriversTimes)) #taking the index of the best time and using it to access the fastest driver

            return self.avail_Driver[Best_Driver]

        else:
            self.waiting_List.append(rider)
            return None


    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        Too many things to be called for an example
        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """
        # TODO

        all_Riders_Patience = []
        if self.waiting_List:

            for rider in self.waiting_List: # goes through the available riders to find the longest waiting rider for the driver

                all_Riders_Patience.append(rider.get_patience()) #adding all the rider patience times to a list

            Best_Rider = all_Riders_Patience.index(max(all_Riders_Patience)) #taking the index of the largest patience and using it to access the longest waiting rider
            return self.waiting_List[Best_Rider]
        else:

            self.avail_Driver.append(driver)
            return None

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        Too many things to be called for an example
        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        # TODO
        self.waiting_List.remove(rider)