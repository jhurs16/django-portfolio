
from django.contrib import admin
from django.urls import path, include 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from projects import views
from aboutme import views as about
from django.conf import settings
from django.conf.urls.static import static
# router = DefaultRouter()
# router.register(r"projects", views.ProjectsViewSet)
# router.register(r"tag", views.TagViewSet)
# router.register(r"skillandexperience", about.SkillAndExperienceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/", include(router.urls)),
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/projects/", include("projects.urls")),
    # path("", include("aboutme.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)