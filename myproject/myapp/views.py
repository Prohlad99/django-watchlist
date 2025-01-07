from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from . import models
from . import serializers


class WatchList(APIView):
    def get(self, request):
        watchlist = models.WatchList.objects.all()
        serializer = serializers.WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class WatchListDetail(APIView):
    def get(self, request, pk):
        watchlist = models.WatchList.objects.get(pk=pk)
        serializer = serializers.WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchlist = models.WatchList.objects.get(pk=pk)
        serializer = serializers.WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        watchlist = models.WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=204)
    
    
class PlatformList(APIView):
    def get(self, request):
        platforms = models.Platform.objects.all()
        serializer = serializers.PlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class PlatformDetail(APIView):
    def get(self, request, pk):
        platform = models.Platform.objects.get(pk=pk)
        serializer = serializers.PlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = models.Platform.objects.get(pk=pk)
        serializer = serializers.PlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        platform = models.Platform.objects.get(pk=pk)
        platform.delete()
        return Response(status=204)
    

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.all()
#         serializer = serializers.MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = serializers.MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'DELETE', 'PUT'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         movie = models.Movie.objects.get(pk=pk)
#         serializer = serializers.MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = models.Movie.objects.get(pk=pk)
#         serializer = serializers.MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'DELETE':
#         movie = models.Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=204)
        