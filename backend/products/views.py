from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        #serializer.save(user = self.request.user)
        #print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None :
            content = title
    
        serializer.save(content= content)
        
    
product_list_create_view = ProductListCreateAPIView.as_view()    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        #lookuo_field = 'pk'
        
        
        
product_detail_view = ProductDetailAPIView.as_view()


""" class ProductListAPIView(generics.ListAPIView):
    
    '''
    NOT USED 
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        #lookuo_field = 'pk' """

@api_view(['GET', 'POST'])     
def product_alt_view (request, pk=None,*args, **kwargs):
    method = request.method 
    
    if method == 'GET':        
        #get request -> detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data            
            return Response(data)        
        
        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    
    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None :
                content = title
            serializer.save(content= content)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status= 400)