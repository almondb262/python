class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        # print("This is", name, "He is", age, "years old", "His field is", tracks, "His result is", score)

        
    def change_name(self, new_name):
        self.new_name = new_name
        print("The student's new name is", new_name)
    def change_age(self, new_age):
        self.new_age = new_age
        print("The student's new age is", new_age)
    def add_track(self, new_tracks):
        self.new_tracks = new_tracks
        print("The student's new tracks are", new_tracks)
    def get_score(self):
        return ("new score is", self.score )


     
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
(Bob.change_name("Peter"))
(Bob.change_age(34))
(Bob.add_track("UI/UX",))
print(f"The student's{Bob.get_score()}marks")
