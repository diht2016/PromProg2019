from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

SECRET_KEY = 'x(#w7=!2b5jim==+jo_syj$m7=h)3nhsfld@w05x$1r$*qhjkv'
DEBUG = True
ROOT_URLCONF = __name__
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': '.'
  }
]

msgs = []

def showPage(request):
  if request.method == 'POST':
    data = request.POST.get('message', '')
    if len(data) > 0 and len(data) < 2000:
      msgs.append(data)
  
  return HttpResponse(render_to_string('main.html', {
    'msgs': msgs
  }, request=request))

urlpatterns = [
  url(r'^$', showPage),
]
