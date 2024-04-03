# TODO: Implement more specific types for the lesson endpoint

from typing import TypedDict
from ..user import API_User
from ..lesson import API_Lesson, API_Lesson_Content


# === GET /api/lessons/<lesson_id> ===
# also used by /api/courses/<course_id>/lessons/<lesson_number>?view=1

class API_GetLesson(TypedDict):
    """
    Response type for GET /api/lessons/<lesson_id>.

    Also used by GET /api/courses/<course_id>/lessons/<lesson_number>?view=1.
    """

    lesson: list[API_Lesson]

class API_GetLesson_Contents(TypedDict):
    """
    Response type for GET /api/lessons/<lesson_id>/contents.
    """

    lesson: list[API_Lesson_Content]

class API_GetLesson_Contents_Challenge(TypedDict):
    """
    Response type for GET /api/lessons/<lesson_id>/contents/challenge.
    """

    challenge: list[API_Lesson_Content]

