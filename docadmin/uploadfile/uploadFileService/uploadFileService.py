from docadmin.models import pdf_uploaded
from django.core.files.storage import FileSystemStorage

class docsUpload:
    # @classmethod
    # def savePdfFile(self, pdfFile,createdDate):
    #     try:
    #
    #         if pdfFile.name.endswith('.pdf'):
    #             saveqry = uploadfile(pdf_name=pdfFile, created_date=createdDate)
    #
    #             saveqry.save()
    #
    #             fs = FileSystemStorage()
    #
    #             pdfname = fs.save(pdfFile.name, pdfFile)
    #
    #             saveqrysuccessobj = {
    #                 'response': "success"
    #             }
    #
    #         else:
    #             saveqrysuccessobj = {
    #                 'errResp': "Upload Only Pdf"
    #             }
    #
    #
    #         return saveqrysuccessobj
    #
    #     except Exception, err:
    #         saveqryfailureobj = {
    #             'response': "Failure"
    #         }
    #         return {'failureobj': saveqryfailureobj}

    @classmethod
    def savePdfFile(self, pdfFile,createdDate):
        try:
            saveqry = pdf_uploaded(pdf_name=pdfFile, created_date=createdDate)

            saveqry.save()

            fs = FileSystemStorage()

            pdfname = fs.save(pdfFile.name, pdfFile)

            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listPdfFile(cls):
        try:
            listqry= pdf_uploaded.objects.all()

            datalist = []

            for values in listqry:
                datalist.append({
                    'pdfId': values.pdf_id,
                    'pdfName': values.pdf_name,
                })

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def delPdfFile(cls, id):
        try:
            delqry = pdf_uploaded.objects.get(pdf_id=id)

            delqry.delete()

            dataobj ={
                'resp' : 'Successfully delete'
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}
