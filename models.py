from django.db import models
from django.utils.translation import gettext_lazy as _


class ErrorDetail(models.Model):
    error_type = models.CharField()
    
    info = models.TextField()
    data = models.TextField()
    
    path = models.URLField(
        null=True, blank=True,
    )
    error_occured_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    user_id = models.CharField(
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('Error')
        verbose_name_plural = _('Errors')
        ordering = ('-id',)

    def __str__(self):
        return f"{self.error_type}-{self.info}"

