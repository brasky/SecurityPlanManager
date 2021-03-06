from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controlsearch/', views.control_search, name='control_search'),
    path('nav-search/', views.nav_search, name='nav_search'),
    path('search/', views.search, name='search'),
    path('teams/add', views.add_team, name='add_team'),
    path('teams/edit', views.edit_teams, name='edit_teams'),
    path('teams/<str:team_name>/', views.view_team, name='view_team'),
    path('teams/', views.teams, name='teams'),
    path('implementations/<int:control_pk>/add/', 
         views.add_implementation, name='add_implementation'),
    path('implementations/<int:control_pk>/edit/', views.edit_implementations, name='edit_implementation'),
    path('implementations/<int:control_pk>/', views.implementations, name='implementations'),
    path('certifications/', views.certifications, name='certifications'),
    path('certifications/add', views.add_certification, name='add_certification'),
    path('certifications/edit', views.edit_certifications, name='edit_certifications'),
    path('certification-test/', views.certifications_test, name='certification-test'),
    path('certifications/<str:certification_name>/', views.view_certification, name='view_certification'),
    path('import/ssp/', views.import_ssp, name='import_ssp'),
    path('import/', views.import_home, name='import_home'),
    path('export/<str:doc_name>/<str:baseline>/<str:format>/', views.export_download, name='export_download'),
    path('export/', views.export_home, name='export_home'),
]
