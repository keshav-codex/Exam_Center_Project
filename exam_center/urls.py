from django.urls import path
from . import views

urlpatterns = [
        path("",views.home, name="home"),
        path("add_exam_center/",views.add_exam_center, name="add_exam_center"),
        path("view_exam_center/",views.view_exam_center, name="view_exam_center"),
        path("update_exam_center/<int:id>",views.update_exam_center, name="update_exam_center"),
        path("delete_exam_center/<int:id>",views.delete_exam_center, name="delete_exam_center"),

]