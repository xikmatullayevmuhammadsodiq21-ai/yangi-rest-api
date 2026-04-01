
from django.urls import path
from api.admin.views.users_list import UserListApiView
from api.admin.views.fintech_muhammadsodiq import FintechMuhammadsodiqApiView
from api.admin.views.fintech_abdunosir import FintechAbdunosirApiView
from api.admin.views.fintech_doston import FintechDostonApiView
from api.admin.views.fintech_azizbek import FintechAzizbekApiView
from api.admin.views.fintech_muhammadrizo import FintechMuhammadrizoApiView
from api.admin.views.fintech_ilyosbek import FintechIlyosbekApiView
from api.admin.views.fintech_hasan import FintechHasanApiView


urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
    path("fintech/muhammadsodiq/", FintechMuhammadsodiqApiView.as_view()),
    path("fintech/ilyosbek/", FintechIlyosbekApiView.as_view()),
    path("fintech/muhammadrizo/", FintechMuhammadrizoApiView.as_view()),
    path("fintech/azizbek/", FintechAzizbekApiView.as_view()),
    path("fintech/doston/", FintechDostonApiView.as_view()),
    path("fintech/abdunosir/", FintechAbdunosirApiView.as_view()),
    path("fintech/hasan/", FintechHasanApiView.as_view()),
]

