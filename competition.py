import json

class Competition:
    def __init__(self, name:str, date:str, numberOfPlaces:str, max_places_required=12):
        self.name = name
        self.date = date
        self.numberOfPlaces = numberOfPlaces
        self.max_places_required = max_places_required
    
    def data(self):
        data = {
            "name": self.name,
            "date": self.date,
            "numberOfPlaces": self.numberOfPlaces,
            "max_places_required": self.max_places_required
        }
        return data

    def remove_places(self, places_required:int):
        self.numberOfPlaces = str(int(self.numberOfPlaces) - places_required)

    def save(self, compettions, index):
        compettions[index] = self.data()
        serialized_compettions = json.dumps({"competitions" : compettions})
        with open('competitions.json', "w") as file:
            file.write(serialized_compettions)
