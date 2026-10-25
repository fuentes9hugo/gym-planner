import json


class MusclesData:
    def __init__(self):
        # File charge
        file=open('data/muscles.json')
        self.muscles = json.load(file)

    # Muscles async data
    async def get_muscles(self):
        return self.muscles

    # Single muscle async data
    async def get_muscle(self,muscle_id: int):
        muscle = None
        # Iterate JSON data
        for item in self.muscles['muscles']:
            # Check id
            if item['id']==muscle_id:
                muscle=item
                break
        return muscle