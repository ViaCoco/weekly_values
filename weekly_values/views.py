from django.shortcuts import render

def post_list(request):
    return render(request, 'weekly_values/post_list.html', {})
