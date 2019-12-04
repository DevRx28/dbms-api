from django.db import models
# from dbapi.settings import *
# Create your models here.


class PlayerManager(models.Manager):
    def get_by_id(self, id):
        queryset = self.get_queryset().filter(id=id)
        if queryset.count() == 1:
            return queryset.first()
        return None

    def featured(self):
        return self.get_queryset().filter(featured=True)


class Player(models.Model):

    # ID = models.IntegerField()
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Photo = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=100)
    Overall = models.IntegerField()
    Potential = models.IntegerField()
    Club = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)
    Wage = models.CharField(max_length=100)
    PreferredFoot = models.CharField(max_length=100)
    InternationalReputation = models.IntegerField()
    WeakFoot = models.IntegerField()
    SkillMoves = models.IntegerField()
    Position = models.CharField(max_length=100)
    JerseyNumber = models.IntegerField()
    Height = models.CharField(max_length=100)
    Weight = models.CharField(max_length=100)
    Crossing = models.IntegerField()
    Finishing = models.IntegerField()
    HeadingAccuracy = models.IntegerField()
    ShortPassing = models.IntegerField()
    Volleys = models.IntegerField()
    Dribbling = models.IntegerField()
    Curve = models.IntegerField()
    FKAccuracy = models.IntegerField()
    LongPassing = models.IntegerField()
    BallControl = models.IntegerField()
    Acceleration = models.IntegerField()
    SprintSpeed = models.IntegerField()
    Agility = models.IntegerField()
    Reactions = models.IntegerField()
    Balance = models.IntegerField()
    ShotPower = models.IntegerField()
    Jumping = models.IntegerField()
    Stamina = models.IntegerField()
    Strength = models.IntegerField()
    LongShots = models.IntegerField()
    Aggression = models.IntegerField()
    Interceptions = models.IntegerField()
    Positioning = models.IntegerField()
    Vision = models.IntegerField()
    Penalties = models.IntegerField()
    Composure = models.IntegerField()
    Marking = models.IntegerField()
    StandingTackle = models.IntegerField()
    SlidingTackle = models.IntegerField()
    GKDiving = models.IntegerField()
    GKkicking = models.IntegerField()
    GKPositioning = models.IntegerField()
    GKReflexes = models.IntegerField()
    GKHandling = models.IntegerField()
    
    objects = PlayerManager()

    # def get_absolute_url(self):
    #     return reverse('details', kwargs={"pk": self.pk})

    def __str__(self):
        return self.Name
