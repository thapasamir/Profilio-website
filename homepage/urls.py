from django.urls import path
from .views import HomePage
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('',HomePage.as_view(),name='home'),
	path('soon..',views.soon,name="soon")
	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)