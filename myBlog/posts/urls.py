from unicodedata import name
from django.urls import path
from . import views

# URL pattern: http://example.com/posts/...
# URL pattern: http://example.com/posts/new
# URL pattern: http://example.com/posts/1
# URL pattern: http://example.com/posts/delete

urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', views.detail, name='detail'),
    path('<delete/<int:id>', views.delete, name='delete'),

]