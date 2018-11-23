from django.urls import path, re_path
from . import views

app_name = 'music'
urlpatterns = [
    #/music
    path('', views.index, name='index'),

    #/music/register
    path('register/', views.register, name='register'),

    #/music/login_user
    path('login_user/', views.login_user, name='login_user'),

    #/music/login_user
    path('logout_user/', views.logout_user, name='logout_user'),

    # /music/712
    path('<int:album_id>/', views.detail, name='detail'),

  #  /music/712/favorite               712---album_id
    path('<int:song_id>/favorite/', views.favorite, name='favorite'),

    # for song
    re_path(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # /music/create_album/
    path('create_album', views.create_album, name='create_album'),

    # /music/712orAlbum_id/create_song/
    path('<int:album_id>/create_song/', views.create_song, name='create_song'),

    # /music/album_id/delete_song/song_id
    path('<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name='delete_song'),

    # /music/album_id/favorite_album
    path('<int:album_id>/favorite_album/', views.favorite_album, name='favorite_album'),

    # /music/album_id/delete_album
    path('<int:album_id>/delete_album/', views.delete_album, name='delete_album'),

    # /music/album/2/
   # path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    #path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]