from django import template
from cadastral.models import Act

register = template.Library()


@register.filter(name='count_objects')
def get_filter_values(value):
    count_objects = value
    remainder = count_objects % 10
    if count_objects >= 10 and count_objects <= 20:
        phrase = f'{str(count_objects)} объектов'
    elif remainder == 1:
        phrase = f'{str(count_objects)} объект'
    elif remainder >= 2 and remainder <= 4:
        phrase = f'{str(count_objects)} объекта'
    elif remainder >= 5 or remainder <= 9:
        phrase = f'{str(count_objects)} объектов'
    return phrase
