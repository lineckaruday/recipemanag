from rest_framework import serializers
from recipe.models import Recipe
from recipe.models import Review
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    # password=serializers.CharField(write_only=True)   #here write only =true coz to hide password while read means while showing user info only shows username and hides pass
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):  # normally when data (password) comes from POST so first it desirialize data then that object.validte and object comes into this class for encryption then object.save here
        user = User.objects.create_user(username=validated_data['username'],
                                        # encrypt is required for password ,without that error while login
                                        password=validated_data['password'])
        user.save()
        return user





class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type']





class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','recipe_name','user','rating','comment']
