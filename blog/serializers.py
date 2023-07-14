import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Category, Post


class PostModel:
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(max_length=1024)


def encode():
    model = PostModel(title='Test title', description="Test Description")
    model_sr = PostSerializer(model)
    print(model_sr.data, type(model_sr), type(model_sr.data), sep="\n")
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    response = io.BytesIO(b'{"title":"Test title","description":"Test Description"}')
    data = JSONParser().parse(response)
    print(data, type(data))
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    print(serializer.data, type(serializer.data))


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField(required=False)
    is_active = serializers.BooleanField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["field"] = f"{instance.title} | {instance.slug}"
        return data

    def save(self):
        title = self.validated_data.get('title')
        slug = self.validated_data.get('slug')
        instance = Category.objects.create(title=title, slug=slug)
        return instance
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance
    

class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"



