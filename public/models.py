from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    visit_count = models.PositiveIntegerField(default=1)
    last_visited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ip_address} visited {self.visit_count} times"

