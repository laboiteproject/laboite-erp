from django.db import models


class Journal(models.Model):
    creation_date = models.DateTimeField('creation date', auto_now_add=True)

class Entry(models.Model): # Écriture en Français
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    ref_date = models.DateField('transaction date')
    explanation = models.CharField(max_length=200) # libellé en Français

class Record(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    account = models.CharField(max_length=20) # numero de compte. ATTENTION : IL EST CONVERTI EN STRING POUR FACILITER LE TRI !
    amount = models.DecimalField(max_digits=11, decimal_places=2) # toujours positif
    DEBIT = 'D'
    CREDIT = 'C'
    SIDE_CHOICES = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )
    side = models.CharField(max_length=1, choices=SIDE_CHOICES, default=DEBIT)

    def is_debit(self):
        return self.side == self.DEBIT

    def is_credit(self):
        return self.side == self.CREDIT
