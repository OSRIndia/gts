from django.db import models

# Create your models here.
class ReferenceType(models.Model):
    code=models.CharField(max_length=10,null=True);
    name=models.CharField(max_length=10,null=True);
    desciption=models.CharField(max_length=100,null=True);
    parentReferenceType=models.ForeignKey('ReferenceType',null=True);

class QuantizedCost(models.Model):
    
    refernce=models.ForeignKey(ReferenceType)
    costType=models.CharField(max_length=50,null=True);
    costQuantity=models.FloatField(null=True);
    costPrizeperpiece=models.FloatField(null=True);
    costtotal=models.FloatField(null=True);
    def computetotalCost(self):
        self.costtotal=self.costPrizeperpiece*self.costQuantity;
