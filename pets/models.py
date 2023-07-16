from django.db import models


class SexTable(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    sex = models.CharField(
        max_length=20, choices=SexTable.choices, default=SexTable.DEFAULT
    )
    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT, related_name="pets"
    )
    traits = models.ManyToManyField("traits.Trait", related_name="pets")

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name} - {self.age}years - {self.weight}kg - {self.sex} - {self.group} - {self.traits}>"


#remember to clean
class TestSSHKeyMod():
    ...
