from ninja import Schema
from typing import List


class AnswersList(Schema):
    title:str
    isTrue:bool


class QuestionOut(Schema):
    title:str
    category:str
    points:int
    seconds:int
    answers:List[AnswersList]
    
class QuestionsOut(QuestionOut):
    id:str

class Questions(Schema):
    question_number:int
    id:str
    
class CategoryOut(Schema):
    category_title:str
    category_image:str
    category_descrition:str = None
    questions_number:int
    questions_id:List[Questions]
    
class SignIn(Schema):
    username=str
    password=str
    
class AuthOut(Schema):
    token: str
    
class ErrorCode(Schema):
    detail: str