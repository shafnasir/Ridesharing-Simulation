class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @rtype: str
        """
        return str(self.row)+","+str(self.column)


    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        """
        return self == other

    def get_row(self):
        """
        This method returns the row number

        @return: row: str
        """

        return self.row

    def get_column(self):
        """
        This method returns the column number

        @return: column: str
        """

        return self.column



def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    """

    x_distance = abs(abs(int(origin.get_row())) - abs(int(destination.get_row())))
    y_distance = abs(abs(int(origin.get_column())) - abs(int(destination.get_column())))

    man_Distance = x_distance + y_distance

    return man_Distance


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    """
    d_Location = ''
    if len(location_str) >= 2:

        d_Location = Location(location_str[0], location_str[2]) # takes the index where the row and column numbers are


    return d_Location


#ori = Location(5,0)
#location = Location(7,2)

#print(manhattan_distance(ori, location))

