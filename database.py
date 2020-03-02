from models import OrbitPath, NearEarthObject

import pandas as pd
from datetime import datetime
class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        self.filename = filename
        self.neo_name = {}
        self.neo_date = {}


    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        df = pd.read_csv(filename)
        for index, row in df.iterrows():

            orbit_path = OrbitPath(**row)

            if not self.neo_name.get(row['name'], None):
                self.neo_name[row['name']] = NearEarthObject(**row)

            near_earth_object = self.neo_name.get(row['name'], None)

            near_earth_object.update_orbits(orbit_path)

            if not self.neo_date.get(row['close_approach_date'], None):
                self.neo_date[row['close_approach_date']] = []

            self.neo_date[row['close_approach_date']].append(near_earth_object)

        print(len(self.neo_date), len(self.neo_name))

        return None