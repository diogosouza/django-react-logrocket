from rest_framework.response import Response
from .models import Student
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .pagination import *



class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentSetPagination



class StudentDetailView(APIView):
    def put(self, request, student_id):
        try:
            student = Student.objects.get(student_id=student_id)
            if student:
                serializer = StudentSerializer(student, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=200)

            return Response(status=404)
        except Exception:
            return Response(status=400)

    def delete(self, request, student_id):
        try:
            student = Student.objects.get(student_id=student_id)

            if student:
                student.delete()

            return Response(status=200)

        except Exception:
            return Response(status=400)


