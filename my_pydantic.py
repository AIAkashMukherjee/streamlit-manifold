from pydantic import BaseModel,ValidationError

data = {
    "name": "Murthy",
    "age": "28",
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "2", "1", 4]
}

class Instructor(BaseModel):
    name:str
    age:str
    course:str
    ratings: list[int] = []

try:
    user = Instructor(**data)
    print(f"Found an Instructor: {user}")
except ValidationError as e:
    print(f"Error validating data: {e}")

