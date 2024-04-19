from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from users.forms import LoginForm, SignUpForm

# 회원가입


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 회원가입 성공 시 로그인 페이지로 이동
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# 로그인


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # 로그인 후 리다이렉션할 페이지를 설정합니다.
                return redirect('home')  # 홈 화면으로 리다이렉션
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# 로그아웃


def user_logout(request):
    logout(request)
    # 로그아웃 후 리다이렉션할 페이지를 설정합니다.
    return redirect('home')  # 홈 화면으로 리다이렉션


def home(request):
    return render(request, 'home.html')
