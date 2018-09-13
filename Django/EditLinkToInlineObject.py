from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


class EditLinkToInlineObject(object):
    def init_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label, instance._meta.model_name), 
            args=[instance.pk])
        if instance.pk:
            return mark_safe('<a href="{}">Edit</a>'.format(url))
        else:
            return ""

class InstanceModelInline(EditLinkToInlineObject, admin.TabularInline):
    model = InstanceModel
    readonly_fields = ('edit_link', )


@admin.register(InstanceModel)
class InstanceModelAdmin(admin.ModelAdmin):
    inline = (InstanceModelInline, )