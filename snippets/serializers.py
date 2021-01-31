from django.contrib.auth.models import User
from pygments import styles
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Serializer classes are very similar to django form classes, and include similar validation flags in the fields
# like the required or read_only flags


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # we can show the owner of a snippet in it's serialized representation:
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets is 'reverse' relationship on the User model, i.e. the User model actually doesn't
    # know about snippets. Only the snippets know about the connection to their owner
    # that's why we need to explicitly define this field, it won't be automatically created
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
