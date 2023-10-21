from django.urls import path
from . import views

urlpatterns = [
    path(
        "create-product/",views.CreateProduct().as_view(),name="create-product"),
    path(
        "update-product/<int:pk>",views.UpdateProduct().as_view(),
        name="update-product"),
    path("products-by-category/<str:category>",views.ListProductsByCategory().as_view(),
         name="products-by-category"),
    path("products-by-stock/<str:order>",views.ListProductsByStock().as_view(),
         name="products-by-stock"),
    path("products-by-price/<str:order>",views.ListProductsByPrice().as_view(),
         name="products-by-price")
]