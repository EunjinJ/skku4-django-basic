import json

from django.http import Http404
from .forms import CommentForm
from .forms import BoardForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Board, Comment

# TODO:
# """
# 1. board_detail에서 댓글을 달 수 있는 form 태그와 input tag 만들기

# 2. form이 submit 되면 요청을 받을 url과 view function 만들기
#     - 1. form에 입력값이 빈 값이면, error를 담아서 html 보내기
#     - 2. form에 입력값이 타당하면, 저장하고 상세페이지 다시 보여주기

# 3. (2)에서 만들어진 url로 (1)의 form에 action 속성에 url기록하기.
# """


def index(request):
    board_list = Board.get_active_list().prefetch_related('comment_set').all()

    return render(request, "board/index.html",
                {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.get(pk=board_id)

    board_history = request.session.get('board_history')
    if not board_history:
        request.session['board_history'] = []
    request.session['board_history'] += [board_id]

    if not (board and board.is_active):
        return Http404("요청하신 페이지가 없습니다.")

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment(
                content=data['content'],
                board_id=board_id
            ).save()
            return redirect(reverse('board:detail',
                                    kwargs={'board_id': board_id}))

    resp = render(request,
                "board/detail.html",
                {'board': board, 'form': form})

    history = request.COOKIES.get('board_history')
    if not history:
        history = []
        history = json.dumps(history)
    history = json.loads(history)
    history += [board_id]
    resp.set_cookie('board_history', json.dumps(history))

    return resp


# def board_detail(request, board_id):
#     errors = []
#     if request.method == 'POST':
#         data = request.POST
#         content = data.get('comment')
#         if content:
#             comment = Comment(
#                 content=content,
#                 board_id=board_id
#             )
#             comment.save()
#         else:
#             errors.append("comment가 비어 있습니다.")

#     board = Board.objects.get(pk=board_id)

#     return render(request,
#                   "board/detail.html",
#                   {'board': board, 'errors': errors})


def board_write(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:index'))

    return render(request,
                  "board/write.html",
                  {'form': form})


def board_edit(request, board_id):
    board = Board.objects.get(id=board_id)
    form = BoardForm(initial={
        'title': board.title,
        'content': board.content,
        'author': board.author
    })
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.author = form.cleaned_data['author']
            board.save()
            return redirect(reverse('board:detail', kwargs={
                'board_id': board_id
            }))
    return render(request,
                  "board/edit.html",
                  {'form': form})


def board_delete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.is_delete = True
    board.save()
    return redirect(reverse('board:index'))


# def board_write(request):
#     if request.method == 'POST':
#         # save model
#         data = request.POST
#         title = data.get('title')
#         content = data.get('content')
#         board = Board(
#             title=title,
#             content=content,
#             author=request.user
#         )
#         board.save()
#         # 문제 X -> index페이지로 이동

#         return redirect(reverse('board:index'))
#     return render(request,
#                   "board/write.html",)

# def index(request):
#     # return HttpResponse("Hello World, I am Younsoo!")
#     sample_list = range(10)

#     return render(request, 'board/index.html',
#                   {'name': '유저', 'sample': sample_list})


# """
# board_list라는 view 함수를 만들고 /board 로 접속하면
# 게시글에 대한 전체 게시글을 리스트 (HTML: ul, li 태그 이용)로 보여주세요.
# """


# def board_list(request):
#     qs = Board.objects.all()

#     html = ""
#     for board in qs:
#         html += f"<li><a href='/board/{board.id}'>\
#             {board.title}\
#                 </a></li>"
#     html = f"<ul>{html}</ul>"

#     return HttpResponse(html)


# """/board/comments로 접속하면 모든 댓글을 조회하도록 해주세요.
#     조회내용에 대한 형식은 다음과 같습니다.
#     (<ul>
#     <li>코멘트id | 댓글내용 | board_id </li>
#     …
#     </ul>)
# """


# def comment_list(request):
#     qs = Comment.objects.all()

#     html = ""
#     for comment in qs:
#         html += f"<li>{comment.id} | \
#             {comment.content} | {comment.board_id} </li>"
#     html = f"<ul>{html}</ul>"

#     return HttpResponse(html)


# """
# 각 게시글을 클릭 가능하게 해주시고,
# 클릭에 대한 url은 /board/<id> 로 해주세요.
# (<id>는 board에 대한 id(pk)값
# """

# # (*args, **kwargs)


# def board_detail(request, board_id):
#     qs = Board.objects.get(id=board_id)
#     comment_list = qs.comment_set.all()

#     html = f"<h1>{qs.title}</h1> \
#         <div>{qs.content}</div>"

#     html += "<ul>"
#     for comment in comment_list:
#         html += f"<li>{comment.content}</li>"
#     html += "</ul>"

#     return HttpResponse(html)