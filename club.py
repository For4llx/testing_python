import json

class Club:
    def __init__(self, name:str, email:str, points:str, places_booked={}):
        self.name = name
        self.email = email
        self.points = points
        self.places_booked = places_booked
    
    def data(self):
        data = {
            "name": self.name,
            "email": self.email,
            "points": self.points,
            "places_booked": self.places_booked
        }
        return data

    def remove_points(self, places_required:int):
        self.points = str(int(self.points) - places_required)

    def add_places_to_competition(self, places_required:int, competition_name:str):
        self.places_booked[competition_name] = str(int(self.places_booked[competition_name]) + places_required)

    def save(self, clubs, index):
        clubs[index] = self.data()
        serialized_clubs = json.dumps({"clubs" : clubs})
        with open('clubs.json', "w") as file:
            file.write(serialized_clubs)
