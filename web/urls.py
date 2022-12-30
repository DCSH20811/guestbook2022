from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include('web.urls')),
    path('', RedirectView.as_view(url='message/')),
    path('accounts/', include('django.contrib.auth.urls')),
]