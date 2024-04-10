from typing import TypedDict
from ..user import API_User
from ..marking import API_Marking

class API_GetMarking(TypedDict):
    """
    Response type for GET /api/markings/.
    """

    attempt_result: list[API_Marking]