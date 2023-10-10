from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # print(request.user)
    print(request.session)
    print("session 확인")
    for k, v in request.session.items():
        print(k, v)

    print("Cookie 확인")
    history = request.COOKIES.get('board_history')
    print(history)
    return render(request, 'user/profile.html')



def profile(request):
    profile = {
        "이름": "정은진",
        "별명": "ej",
    }
    result = ""

    for k, v in profile.items():
        result += f"<li>{k}: {v}</li>"

    html = f"""
        <h1>나의 정보</h1>
        <ul>
            {result}
        </ul>
    """

    # print(dir(request))
    request_attrs = dir(request)

    for attr in request_attrs:
        if attr.startswith("_"):
            continue
        print(attr, getattr(request, attr))
        print('-'*10)

    return HttpResponse(html)