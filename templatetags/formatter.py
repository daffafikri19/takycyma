from django import template

register = template.Library()

@register.filter(name='format_rupiah')
def format_rupiah(value):
    try:
        value = float(value)
        return "Rp. {:,.2f}".format(value)
    except (ValueError, TypeError):
        return value
