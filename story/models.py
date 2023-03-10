from django.db import models
from django.utils.translation import gettext_lazy as _

class Ingredient(models.Model):
    UNIT_CHOICE = (
        (1, _('ml')),
        (2, _('g')),
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    sku_number = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(
        'supplier.Supplier',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    unit = models.PositiveSmallIntegerField(
        choices=UNIT_CHOICE,
        default=1,
    )

    @property
    def label(self):
        return f'{self.name} - {self.quantity} {self.get_unit_display()}'

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.label
