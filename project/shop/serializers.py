# from rest_framework import generics, permissions, serializers
# from django.contrib.auth.models import User, Group

from rest_framework import serializers
from django.contrib.auth.models import User

from shop.models import Category, Product, Review, ProductSpecification, Image
from djoser.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSpecification(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        many=False, slug_field='name', source='specification', read_only=True)

    class Meta:
        model = ProductSpecification
        fields = ['value', 'name']


class PureReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = ['user', 'title', 'text', 'rate', 'product']

# care about cycle deps


class ReviewWithoutProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'title', 'text', 'rate']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    reviews = ReviewWithoutProductSerializer(many=True, read_only=True)
    specification = ProductSpecification(many=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'reviews', 'specification',
                  'short_description', 'description', 'images', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'product', 'title', 'text', 'rate']
