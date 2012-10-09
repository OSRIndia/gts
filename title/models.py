from django.db import models
from master.models import ReferenceType

# Create your models here.
class Title(models.Model):
    name=models.CharField(max_length=100,null=False);
    releaseDate=models.DateField(null=False);
    def __unicode__(self):
        return self.name
 
class FilmTitle(Title):
    FilmNumber=models.CharField(max_length=100,null=False);
    
    version_status=(
         (u'ORIGINAL,2D',u'ORIGINAL,2D'),
         (u'ORIGINAL,3D',u'ORIGINAL,3D'),
         (u'LOCALIZED,2D',u'LOCALIZED,2D'),
         (u'LOCALIZED,3D',u'LOCALIZED,3D'),
       )
    def __unicode__(self):
        return self.FilmNumber
    
    
class TrailerTitle(Title):
    TrailerNumber=models.CharField(max_length=100,null=False);
   
    def __unicode__(self):
        return self.TrailerNumber


    
