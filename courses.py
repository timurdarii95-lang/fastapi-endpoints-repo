from os.path import defpath

from fastapi import FastAPI, Body

app = FastAPI()

COURSES = [
    {'title': 'Python Fundamentals', 'trainer': 'Alex', 'level': 'beginner'},
    {'title': 'Java Backend', 'trainer': 'Maria', 'level': 'intermediate'},
    {'title': 'QA Automation', 'trainer': 'Victor', 'level': 'beginner'},
    {'title': 'Web Basics', 'trainer': 'Elena', 'level': 'beginner'},
    {'title': 'Databases', 'trainer': 'Andrei', 'level': 'intermediate'},
    {'title': 'System Design', 'trainer': 'Irina', 'level': 'advanced'}
]

@app.get('/courses')
async def read_all_courses():
    return COURSES



@app.get('/courses/{course_title}')
async def read_course(course_title: str):
    for course in COURSES:
        if course.get('title').casefold() == course_title.casefold():
            return course


@app.get('/courses/bytrainer/')
async def read_courses_by_trainer(trainer: str):
    courses_to_return = []
    for course in COURSES:
        if course.get('trainer').casefold() == trainer.casefold():
            courses_to_return.append(course)

    return courses_to_return


@app.post('/courses/create_course')
async def create_course(new_course=Body()):
    COURSES.append(new_course)