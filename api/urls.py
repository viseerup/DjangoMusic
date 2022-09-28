from django.urls import path
from .views import RoomView

urlpatterns = [
    
    #path('', main )
    path('', RoomView.as_view() )
]
