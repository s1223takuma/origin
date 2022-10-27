from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "blog/index.html")

def detail(request):
    return HttpResponse("detail page")

class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")


class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")

    # post を追加
    def post(self, request):
        # ユーザー情報を保存する
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        # 登録完了画面を表示する
        return render(request, "blog/register_success.html")
# django であらかじめ用意されている LoginView を利用したいので、 import しておきます

# LoginView を継承したうえで、一部設定を変更
class AccountLoginView(LoginView):
    """ログインページのテンプレート"""
    template_name = 'blog/login.html'

    def get_default_redirect_url(self):
        """ログインに成功した時に飛ばされるURL"""
        return "/blog"


# LoginRequiredMixin を追加
# 実は、Python では複数のクラスを継承できます
# 順番は必ず LoginRequiredMixin, View の順番にしてください
class MypageView(LoginRequiredMixin, View):
    # ログインしていない場合に飛ばすページの設定
    login_url = '/blog/login'

    def get(self, request):
        return render(request, "blog/mypage.html")