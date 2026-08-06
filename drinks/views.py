from .models import Drink
from .serializers import DrinkSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()

        serializer = DrinkSerializer(drinks, many=True)

        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'success': True,
                'message': 'Drink created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Failed to create drink',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Drink not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)

        return Response({
            'success': True,
            'message': 'Drink retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'success': True,
                'message': 'Drink updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'message': 'Failed to update drink',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        
        return Response({
            'success': True,
            'message': 'Drink deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

