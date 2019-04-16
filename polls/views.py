from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요! 이곳은 설문 조사 페이지의 기본 화면입니다.")
