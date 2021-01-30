from django.contrib.auth.models import User
from pygments import styles
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Serializer classes are very similar to django form classes, and include similar validation flags in the fields
# like the required or read_only flags


class SnippetSerializer(serializers.ModelSerializer):
    # we can show the owner of a snippet in it's serialized representation:
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    # snippets is 'reverse' relationship on the User model, i.e. the User model actually doesn't
    # know about snippets. Only the snippets know about the connection to their owner
    # that's why we need to explicitly define this field, it won't be automatically created
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
