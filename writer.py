from enum import Enum
import pandas as pd

class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.
        if format == self.output_formats[0]:
            try:
                print(data)
                return True
            except IOError as e:
                return False

        elif format == self.output_formats[1]:
            try:
                ids = []
                names = []
                diameter_min_kms = []
                orbits = []
                orbit_dates = []

                for neo_object in data:
                    ids.append(neo_object.id)
                    names.append(neo_object.name)
                    diameter_min_kms.append(neo_object.diameter_min_km)
                    orbits.append([orbit.neo_name for orbit in neo_object.orbits])
                    orbit_dates.append([orbit.close_approach_date for orbit in neo_object.orbits])

                df = pd.DataFrame({'id': ids, 'name': names, 'diameter_min_km': diameter_min_kms,
                                   'orbits': orbits, 'orbit_dates': orbit_dates})
                df.to_csv('data/neo_data_results.csv')
                return True
            except IOError as e:
                return False
        else:
            return False