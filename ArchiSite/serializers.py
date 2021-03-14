from rest_framework import serializers

from .models import Portfolio, Services, NewsletterList, Applications, Blog

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class NewsletterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsletterList
        fields = '__all__'

class ApplicationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'

class BlogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
