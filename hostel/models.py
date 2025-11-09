from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Block(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    block_name = models.CharField(max_length=50, unique=True)  # e.g., B1, B2, B3, G1, G2, G3
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.block_name} ({self.get_gender_display()})"

    class Meta:
        ordering = ['block_name']


class Floor(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='floors')
    floor_number = models.IntegerField()

    def __str__(self):
        return f"{self.block.block_name} - Floor {self.floor_number}"

    class Meta:
        ordering = ['block', 'floor_number']
        unique_together = ['block', 'floor_number']


class Room(models.Model):
    room_number = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    capacity = models.IntegerField(default=1)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='booked_rooms')

    def __str__(self):
        return f"{self.floor.block.block_name} - {self.room_number}"

    class Meta:
        ordering = ['floor', 'room_number']
        unique_together = ['floor', 'room_number']
