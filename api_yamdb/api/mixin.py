from rest_framework import mixins, viewsets


class MyCreateListDestroyClass(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    "Кастомный миксин класс"
    pass
