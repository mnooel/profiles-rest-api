from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers as profiles_serializers
from . import models as profiles_model
from . import permissions as profiles_permissions


#  ******************************************************************************************************************  #


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = profiles_serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Users HTTPS methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is Mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete and object"""
        return Response({'method': 'delete'})


#  ******************************************************************************************************************  #


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = profiles_serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_updates)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID."""
        return Response({'https_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object."""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partially updating an object."""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object."""
        return Response({'http_method': 'DELETE'})


#  ******************************************************************************************************************  #


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""

    serializer_class = profiles_serializers.UserProfileSerializer
    queryset = profiles_model.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (profiles_permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )
