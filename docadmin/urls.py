from django.conf.urls import url
from docadmin import views
from docadmin.registeruser.registerusercontroller import registerusercontroller
from docadmin.login.loginController import loginController
from docadmin.uploadfile.uploadFileController import uploadFileController

urlpatterns = [
    # First time rendering from django side
    url(r'^$', views.loginView.as_view()),

    # register user urls starts
    url(r'^api/saveuser/$', registerusercontroller.saveUser),
    url(r'^api/listusers/$', registerusercontroller.listUsers),
    url(r'^api/deleteusers/$', registerusercontroller.deleteUser),
    url(r'^api/geteditdata/$', registerusercontroller.getEditData),
    url(r'^api/updateuser/$', registerusercontroller.updateUser),
    # register user urls ends

    # Login user Starts
    url(r'^api/checkemail/$', loginController.checkEmail),
    url(r'^api/updatepassword/$', loginController.updatePassword),
    url(r'^api/login/$', loginController.loginUser),
    # Login user Ends

    #Dashboard starts
    url(r'^api/fetchusercount/$', registerusercontroller.userCount),
    #Daashboard ends

#     upload pdf
    url(r'^api/savepdf/$', uploadFileController.savepdf),
    url(r'^api/listpdf/$', uploadFileController.listPdf),
    url(r'^api/delpdf/$', uploadFileController.delPdf),




]