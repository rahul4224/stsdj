from django.http import HttpResponse
from django.shortcuts import redirect


def OnlyAuth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_cdc:
                return redirect('index')
            elif request.user.is_teacher:
                return redirect('Professor')
            elif request.user.is_student:
                return redirect('student')
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func