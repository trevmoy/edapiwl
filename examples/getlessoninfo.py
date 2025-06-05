from edapi import EdAPIWL

ed = EdAPIWL()
ed.login()

# Note that list_lessons() will only return data if a course a user is enrolled in has lessons set up.
lesson_info = ed.list_lessons()

print(f"Lesson 1: {lesson_info['lessons'][0]['title']}")