from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import signup, ActivitiesView, ActivityDetail, logout_view, index, community, quit_process, out_community, \
    InfoOutCreateView, CommissionMembersView, contact, created

app_name= 'activity'

urlpatterns = [
    path('', index, name="home"),
    path('community/',community,name="community"),
    path('activites/',ActivitiesView.as_view(),name='activites'),
    path('detail-<str:pk>/for-an-activity/', ActivityDetail.as_view(), name='detail'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("quit_process/",quit_process, name='quit'),
    path('out_community/',out_community, name='out'),
    path('reason/', InfoOutCreateView.as_view(),name='reason'),
    path('members-commission/<str:commission>/', CommissionMembersView.as_view(), name='members_commission'),
    path('contact/', contact, name='contact'),
    path('path/', created, name='created' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)