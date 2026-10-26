import json


# Function maker for get all items
def make_collection_getter(key: str):
    async def get_items(self, skip, total, all_items):
        data = getattr(self, key)
        return data if all_items else {key: data[key][skip:skip + total]}

    return get_items

# Function maker for get a single item
def make_single_item_getter(key: str):
    async def get_item(self, item_id: int):
        data = getattr(self, key)

        for item in data[key]:
            if item.get("id") == item_id:
                return item
        return None

    return get_item


class RoutineData:
    def __init__(self):
        # File charge
        with open("data/muscles.json", encoding="utf-8") as file:
            self.muscles = json.load(file)

        with open("data/exercises.json", encoding="utf-8") as file:
            self.exercises = json.load(file)

    # MUSCLES
    get_muscles = make_collection_getter("muscles")
    get_muscle = make_single_item_getter("muscles")

    # Get a muscle from an exercise
    async def get_muscle_exercise(self, exercise_id: int, muscle_id: int):
        exercise = await self.get_exercise(exercise_id)

        if exercise:
            for item in exercise["muscles"]:
                if item.get("id") == muscle_id:
                    return await self.get_muscle(muscle_id)

        return None
    
    # EXERCISES
    get_exercises = make_collection_getter("exercises")
    get_exercise = make_single_item_getter("exercises")