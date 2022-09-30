from django.contrib.auth import get_user_model
from typing import List
from ninja import Router
from django.conf import settings

from computiq.models import *
from computiq.schema import *
from computiq.authorization import *
from config.settings import BASE_DIR


computiq_router = Router(tags=['quiz_app'])

User = get_user_model()
#all ques, category,quesion with id

@computiq_router.get("/get_all_questions", response=List[QuestionsOut],auth=AuthBearer())
def get_all_questions(request):
    questions=Question.objects.select_related('category').all()
    result=[]
    for question in questions:
        answers=question.answer.all()
        result.append({
            'id': str(question.id),'title': question.title, 'category': question.category.category_title,'points':question.points,'seconds':question.seconds,'answers':list(answers),
        })
    return result

@computiq_router.get("/get_one_question/{id}", response=QuestionOut,auth=AuthBearer())
def get_one_question(request,id:str):
    question=Question.objects.select_related('category').get(id=id)
    answers=question.answer.all()
    print(question.title)
    return {
        'title': question.title, 'category': question.category.category_title,'points':question.points,'seconds':question.seconds,'answers':list(answers),
        }
    
@computiq_router.get("/get_all_categories", response=List[CategoryOut],auth=AuthBearer())
def get_all_categories(request):
    categories=Category.objects.all()
    result=[]
    for category in categories:
        questionsId=[]
        initial=1
        questions=category.category.all()
        for question in questions:
            questionsId.append({
                'question_number': initial,'id':str(question.id)
                })
            initial +=1
    
        result.append({
            'category_title': category.category_title,'category_image':category.category_image.url,'category_descrition':category.category_descrition,'questions_number':len(questions),'questions_id':questionsId
        })        
    return result

@computiq_router.post("/signin",response={
    200: AuthOut,
    404: ErrorCode,
    401: ErrorCode
})
def signin(request, username:str, password:str):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    else:
        if user.check_password(password):
            token = create_token_for_user(user)

            return {
                'token': token,
            }
        else:
            return 401,{'detail': 'password incorrect'}
    

    if not user:
        return 404, {'detail': 'User is not registered'}
