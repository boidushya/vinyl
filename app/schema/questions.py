from pydantic import BaseModel


class GenerateQuestions(BaseModel):
    track_ids: list
    room_id: str
    limit: int


class FetchQuestions(BaseModel):
    room_id: str


class CheckAnswer(BaseModel):
    question_id: str
    answer: str
