class NumChallenges():
    def __init__(self):
        self.nums = [12, 5, 9, 21, 7, 12, 5]
        self.cleaned_list = []

    def duplicate_remover(self):
        for num in self.nums:
            if num not in self.cleaned_list:
                self.cleaned_list.append(num)
        return  self.cleaned_list



    def max_num_finder(self):
        max_num = self.nums[0]
        for num in self.nums:
            if num > max_num:
                max_num = num
        return max_num


    def min_num_finder(self):
        min_num = self.nums[0]
        for num in self.nums:
            if num < min_num:
                min_num = num
        return min_num


    def num_counter(self):
        num_dict = dict((num,0) for num in self.nums)
        for num in self.nums:
            num_dict[num] += 1
        for key, value in num_dict.items():
            print(f"{key:<3}:{value}")

session1 = NumChallenges()

db = {}
def add_student(db):
    try:
        entry_count = int(input("Enter number of entries: "))
        for x in range(entry_count):
            student_name = input("\nEnter Student name: ")
            if not db[student_name]:
                db[student_name] = {}
            courses_offered = int(input("Enter amount of courses offered: "))
            for y in range(courses_offered):
                course_name = input("\nEnter Course name: ")
                try:
                    score = float(input("Enter Score: "))
                    db[student_name][course_name] = score

                except ValueError:
                    print("Invalid entry")
    except ValueError:
        print("Invalid entry")











def update_score(db):
    student_name = input("\nEnter Student name: ")
    if student_name not in db:
        print("Student doesn't exist")
    else:
        course_name = input("\nEnter Course name: ")
        if course_name not in db[student_name]:
            print("Course not found")
        else:
            updated_score = float(input("Enter Updated Score: "))
            db[student_name][course_name] = updated_score
            print("Records successfully updated")

    print(db)

def get_average_score(db):
    student_name = input("\nEnter Student name: ")
    if student_name not in db:
        print("Student doesn't exist")
    else:
        average_score = sum(value for key, value in db[student_name].items())/len(db[student_name])

        print(average_score)


add_student(db)
update_score(db)
get_average_score(db)




