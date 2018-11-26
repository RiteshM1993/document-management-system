from docadmin.models import registeruser
from  docadmin.models import pdf_uploaded

from django.core.exceptions import ValidationError


class docsUser:
    @classmethod
    def saveDocsUsers(self, username, email, password, createdDate):
        try:

            saveqry = registeruser(user_name=username, user_email=email, created_date=createdDate,
                                       user_password=password)
            saveqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def DocsUserCount(cls):
        try:
            countuserqry = registeruser.objects.count()
            countpdfqry = pdf_uploaded.objects.count()
            dataobj = {
                'userCount': countuserqry,
                'pdfCount' : countpdfqry,
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return {'failureobj': saveqryfailureobj}

    @classmethod
    def DocsUserList(cls):
        try:
            getqry = registeruser.objects.all()

            datalist = []

            for values in getqry:
                datalist.append({
                    'userId': values.user_id,
                    'userName': values.user_name,
                    'userEmail': values.user_email,
                })

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return {'failureobj': saveqryfailureobj}


    @classmethod
    def DocsUserDelete(cls, id):
        try:
            delqry = registeruser.objects.get(user_id=id)

            delqry.delete()

            datatobj={
                'data': 'success',
            }

            return datatobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

    @classmethod
    def getEditUserData(cls, id):
        try:
            getuserqry = registeruser.objects.get(user_id=id)

            datalist = [{
                'userId': getuserqry.user_id,
                'userName': getuserqry.user_name,
                'userEmail': getuserqry.user_email,
            }]

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

    @classmethod
    def updateUserData(cls, id, username, email, dob, modifiedDate):
        try:
            getuserdata = registeruser.objects.get(user_id=id)

            getuserdata.user_name = username
            getuserdata.user_email = email
            getuserdata.modified_date = modifiedDate

            getuserdata.save()

            dataobj = {
                'data' : 'success',
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

