from rest_framework import status
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        # self.list provided by ListModelMixin
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # self.create provided by CreateModelMixin
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        # self.retrieve provided by RetrieveModelMixin
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # self.update provided by UpdateModelMixin
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # self.delete provided by DestroyModelMixin
        return self.delete(request, *args, **kwargs)

