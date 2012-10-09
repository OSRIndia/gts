from django.db import models
from master.models import ReferenceType


class EstimateCost(object):
    pass

class ReferenceType(models.Model):
    estimateCost=Relationship=models.ForeignKey(EstimateCost)
    code=models.CharField(max_length=10,null=True,blank=True);
    name=models.CharField(max_length=10,null=True,blank=True);
    desciption=models.CharField(max_length=100,null=True,blank=True);
    parentReferenceType=models.ForeignKey('ReferenceType',null=True,blank=True);

class QuantizedCost(models.Model):
    estimateCost=Relationship=models.ForeignKey(EstimateCost)
    refernce=models.ForeignKey(ReferenceType)
    costType=models.CharField(max_length=50,null=True);
    costQuantity=models.FloatField(null=False);
    costPrizeperpiece=models.FloatField(null=False);
    costtotal=models.FloatField(null=False);
    def computetotalCost(self):
        self.costtotal=self.costPrizeperpiece*self.costQuantity;


class PrintCost(EstimateCost):
        version=models.Model(ReferenceType);
   


class SubDistributionCost(EstimateCost):
    pass


class TrailerCost(EstimateCost):
    pass


class OtherCost(EstimateCost):
    pass



# Create your models here.
class Estimate(models.Model):
    PrintCost=models.Model(PrintCost);
    SubDistributionCost=models.Model(SubDistributionCost);
    TrailerCost=models.Model(TrailerCost);
    OtherCost=models.Model(OtherCost);
    version=models.Model(ReferenceType);
