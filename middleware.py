import sys
import traceback

from django.utils.deprecation import MiddlewareMixin

from error_report.models import ErrorDetail
from error_report.settings import ERROR_DETAIL_SETTINGS

def handle_save(exception, request=None):
    if ERROR_DETAIL_SETTINGS:
        if request:
            path = request.build_absolute_uri()
            user_id = request.user.id if request.user.is_authenticated else None
        else:
            path = None
            user_id = None
        
        exc_type, exc_value, _ = sys.exc_info()
        ErrorDetail.objects.create(
            error_type=exc_type.__name__,
            path=path,
            user_id=user_id,
            info=exc_value,
            data=traceback.format_exc(),
        )

class ExceptionProcessor(MiddlewareMixin):
    def process_exception(self, request, exception):
        handle_save(exception, request)
