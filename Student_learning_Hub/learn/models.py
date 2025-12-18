from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
'''
user    (provided by django )
LearningResource  (course , Video , Article )
LearningPath       (grouping resources)
LearningPathItem        (ordering resources , preventing duplication)
'''

resource_type_choices = [
    ("course", "Course"),
    ("video", "Video"),
    ("article", "Article"),
    ("practice", "Practice"),
]

status_choice=[
    ("Planned","Planned"),
    ("Inprogress","Inprogress"),
    ("Completed","Completed"),
    ("Dropped","Dropped"),
]

class LearningResource(models.Model):
    
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    platform = models.CharField(max_length=50)
    resource_type = models.CharField(choices=resource_type_choices,default="course", max_length=50)
    subject = models.CharField(max_length=50)
    status = models.CharField(choices=status_choice, default="Planned", max_length=50)
    progress = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)  # set once when created
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    

class LearningPath(models.Model):
    name = models.CharField( max_length=50)
    description= models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   #import user
    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)  # set once when created
    updated_at = models.DateTimeField(auto_now=True)      # updates every save
    
    def __str__(self):
        return self.name
    

    
class LearningPathItem(models.Model):
    path = models.ForeignKey("LearningPath",on_delete=models.CASCADE)
    resource = models.ForeignKey("LearningResource", on_delete=models.CASCADE)
    order = models.IntegerField()
    class Meta:
        unique_together = ('path', 'resource') 
    
    def __str__(self):
        return f"{self.path.name} - {self.resource.title} (Order: {self.order})"

    