from django.shortcuts import render
from recipe.models import Recipe
from recipe.models import Review
from recipe.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import mixins,generics,viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import Http404



# Create your views here.




# func based view -------------------------------------------------------------------------

@api_view(['GET','POST'])
def allrecipe(request):

    if (request.method == "GET"):
        r=Recipe.objects.all()
        rs = RecipeSerializer(r, many=True)
        return Response(rs.data)
                  # return Response(status=status.HTTP_400_BAD_REQUEST)

    elif (request.method == "POST"):
        r = RecipeSerializer(data=request.data)
        if r.is_valid():  # after validation of client it will save into database table student
            r.save()
            return Response(r.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



# func based pk based api view----------------------------------------------------------


@api_view(['GET','PUT','DELETE'])
def recipedetails(request, pk):

    try:
        r = Recipe.objects.get(pk=pk)  # primary key based (we can use id also same as pk primary key)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == "GET"):
        rs = RecipeSerializer(r)
        return Response(rs.data)

    elif (request.method == "PUT"):
        rs = RecipeSerializer(r, data=request.data)
        if rs.is_valid():
            rs.save()
            return Response(rs.data, status=status.HTTP_201_CREATED)

    elif (request.method == "DELETE"):
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)




# Userview set Register ------( User Register)----POST-----------------------------------------------------------------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer





 # Login  Userview set ---------(user Login)----POST---------------------------------------------------------------------------------------------


 # here for login we use Token Authentication (there are three more auth but here we use token auth)
 # for token auth add in settings.py (added there)
 # url path is added (builtin url path)
 # for creating a token table to save that login token - makemigartion and migrate after setting path and settings for authtoken
 # a token is - data passed from backend when the login is successfull (to show in client side that their data passed to backend for check login is success so a token is passed to client side)





# Logout  user ---------GET------------------------------------------------------------------------------------------

class user_logout(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg:Logout Successfully'},status=status.HTTP_200_OK)

    # after login only logout works so authorization and token to be passed as headers to logout
    # this is GET request api method
    # when login a token is passed into client side and that token is saved in backened api side
    # so after logout that token must be deleted from backend table





# Review create POST and GET ----------------------------------------------------------------------------------------

class allrev(APIView):
    # permission_classes = [IsAuthenticated, ]
    def get(self,request):
        r=Review.objects.all()
        revser=ReviewSerializer(r,many=True)
        return Response(revser.data)

    def post(self,request):                                # POST for review generating and save ein table
        r=ReviewSerializer(data=request.data)
        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)

        return Response(status.HTTP_400_BAD_REQUEST)



class detailrev(APIView):
    # permission_classes = [IsAuthenticated, ]
    def get_object(self,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        r=self.get_object(pk)
        rev=Review.objects.filter(recipe_name=r)
        revser=ReviewSerializer(rev,many=True)
        return Response(revser.data)




# filter based cuisine type----------------------------------------------------------

class cuisinefilter(APIView):
    def get(self,request):
        query=self.request.query_params.get('cuisine')          # here cuisine is keyword that client side passing data through this keyword name
        recipes=Recipe.objects.filter(cuisine=query)            # eg : in POST MAN params  :{ cuisine : chinese }
        r=RecipeSerializer(recipes,many=True)
        return Response(r.data)



# filter based meal type----------------------------------------------------------

class mealfilter(APIView):
    def get(self,request):
        query=self.request.query_params.get("mealtype")          # here mealtype is keyword that client side passing data through this keyword name
        meals=Recipe.objects.filter(meal_type=query)             # eg : in POST MAN params :{ mealtype : snacks }
        r=RecipeSerializer(meals,many=True)
        return Response(r.data)



# filter based ingredients----------------------------------------------------------

class ingredientsfilter(APIView):
    def get(self,request):
        query=self.request.query_params.get("ingredients")          # here ingredients is keyword that client side passing data through this keyword name
        ingd=Recipe.objects.filter(recipe_ingredients=query)        # eg : in POST MAN params  :{ ingredients : butter }
        r=RecipeSerializer(ingd,many=True)
        return Response(r.data)
