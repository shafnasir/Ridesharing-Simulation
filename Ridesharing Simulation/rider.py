"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    # TODO
    """A rider for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type origin: Location
        The current location of the rider.
    @type destination: location
        The end location of the rider
    @type status: str
        A string representing the riders status
    @type patience: int
        A integer representing the patience of the rider
    """

    def __init__(self,identifier, origin, destination, status, patience):
        """
        @type self: Rider
        @param identifier: str
        @param origin: location
        @param destination: location
        @param status: str
        @param patience: int
        @return: None
        """
        self.identifier = identifier
        self.origin = origin
        self.destination = destination
        self.patience = patience
        self.status = status

    def __str__(self):

        """Return a string representation.

        @type self: Rider
        @rtype: str
        """

        return str(self.identifier) + ", " + str(self.origin) + ", " + str(self.destination) + ", " + str(self.status) + ", " + str(self.patience)

    def get_destination(self):
        """
        This method returns the riders destination

        @return: destination: location
        """

        return self.destination

    def get_patience(self):
        """
        This method returns the riders patience

        @return: patience: int
        """

        return self.patience

    def get_status(self):
        """
        This method returns the riders status

        @return: status: str
        """

        return self.status

    def get_origin(self):
        """
        This method returns the riders original location

        @return: origin: location
        """

        return self.origin






