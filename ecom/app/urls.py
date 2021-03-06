from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.forms import LoginForm, ChangePasswordForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>/', views.laptop, name='laptopdata'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>/', views.topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomweardata'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    # used builtin user=> Registration, login, logout,  password_change and password_reset class

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(next_page="login"), name='logout'),

    path("accounts/password_change/", auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html", form_class=ChangePasswordForm, success_url="/accounts/password_change_done/"), 
    name="password_change"),

    path("accounts/password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name="app/password_change_done.html"), name="password_change_done"),

    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),

    path("accounts/password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name="password_reset_done"),

    path("accounts/password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),

    path("accounts/password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"), name="password_reset_complete"),

    # ********************************************************************************************

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


