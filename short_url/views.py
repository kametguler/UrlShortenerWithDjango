from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from short_url.models import ShortUrlModel
from short_url.serializers import ShortUrlSerializer
from utils.RandomCodeGenerator import generator
from django.http import HttpResponseRedirect

class ShortUrlView(ModelViewSet):
    lookup_field = 'code'
    queryset = ShortUrlModel.objects.all()
    serializer_class = ShortUrlSerializer

    def generate_code(self):
        generated_code = generator.generate_random_string()
        is_exists = self.get_queryset().filter(code=generated_code)

        if is_exists.exists():
            self.generate_code()
        else:
            return generated_code

    def perform_create(self, serializer):
        code = self.request.data.get('code', None)
        if code == "" or code is None:
            code = self.generate_code()
            serializer.save(code=code)
        else:
            serializer.save()

    def go_short_url(self, request, *args, **kwargs):
        code = self.kwargs.get('code', None)
        if code is not None:
            short_url = self.get_queryset().filter(code=code).last()
            if short_url:
                return HttpResponseRedirect(short_url.__str__())
            else:
                return Response({"message": "short link is not found"}, status=404)
        else:
            return Response({"message": "error"}, status=400)
