from django.urls import path, include

import blog.views

urlpatterns = [
       #path('detail', blog.views.get_detail_page)
       path('index',blog.views.get_index_page),
       path('detail/<int:article_id>',blog.views.get_detail_page)
]