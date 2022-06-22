from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
]