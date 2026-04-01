
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class FintechDostonApiView(APIView):

    def get(self, request):
      
        data = {
            "message": "ok",
            "status": "backenddan salomlar",
            "fintech_doston": []
        }
        return Response(data, status=status.HTTP_200_OK)
    
