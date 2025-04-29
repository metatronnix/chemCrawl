from dataclasses import dataclass, field
from typing import List, Optional
from django.db import models

class Compound(models.Model):
    cid =  models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molecular_formula = models.CharField(max_length=100, blank=True)
    molecular_weight = models.FloatField(null=True, blank=True)
    canonical_smiles = models.TextField(blank=True)
    inchi = models.CharField(max_length=255)
    smiles = models.CharField(max_length=255)
    inchikey = models.CharField(max_length=255)
    iupacname =  models.CharField(max_length=255)
    exactmass =  models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}: {self.cid}"