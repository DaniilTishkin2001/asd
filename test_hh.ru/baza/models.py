from mptt import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db import models




class FIASNode(MPTTModel, models.Model):
    HOUSE_TYPE = "house"
    STREET_TYPE = "street"
    CITY_DISTRICT_TYPE = "city_district"
    CITY_TYPE = "city"
    FEDERAL_DISTRICT_TYPE = "federal_district"
    COUNTRY = "country"


    type_choices = [
        (HOUSE_TYPE, ("house")),
        (STREET_TYPE, ("street")),
        (CITY_DISTRICT_TYPE, ("city_district")),
        (CITY_TYPE, ("city")),
        (FEDERAL_DISTRICT_TYPE, ("federal_district")),
        (CITY_TYPE, ("city"))
    ]

    name = models.CharField(max_length=100, help_text = ("Name of FIAS node."))
    type = models.CharField(
        choices=type_choices, max_length=50, help_text = ("FIAS node type")
    )
    parent = TreeForeignKey("self",on_delete=models.CASCADE, null=True,blank=True, related_name="children")


    class MPTTMeta:
        order_insertion_by = ["name"]


