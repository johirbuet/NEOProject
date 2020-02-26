class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.orbits = []
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', 'No Name Found')
        self.diameter_min_km = float(kwargs.get('estimated_diameter_min_kilometers', 0))
        self.is_potentially_hazardous_asteroid = kwargs.get('is_potentially_hazardous_asteroid', False)

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        # TODO: How do we connect orbits back to the Near Earth Object?
        self.orbits.append(orbit)

    def __repr__(self):
        return f'NearEarthObject id:{self.id} name:{self.name} \
                                    orbits: {[orbit.neo_name for orbit in self.orbits]} \
                                    orbit_dates:{[orbit.close_approach_date for orbit in self.orbits]}'




class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.name = kwargs.name
        self.miss_km = kwargs.miss_km
        self.orbit_date = kwargs.orbit_date
