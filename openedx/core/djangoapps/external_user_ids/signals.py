from logging import getLogger

from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import CourseEnrollment
from openedx.core.djangoapps.catalog.utils import get_program_details_for_course_run

LOGGER = getLogger(__name__)


@receiver(post_save, sender=CourseEnrollment)
def create_external_id_for_microbachelors_program(sender, instance, **kwargs):
    """
    Watches for post_save signal for creates on the CourseEnrollment table.
    Generate an External ID if the Enrollment is in a MicroBachelors Program
    """
    LOGGER.info('***** TEST: in receiver 1!!!')
    if kwargs.get('course_id') and instance.user:
        user_id = instance.user.id
        LOGGER.info('***** TEST: in receiver!!!')

