from django.db import models


class Journal(models.Model):
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    title = models.CharField(max_length=200, default='journal name')

    def __str__(self):
        return self.title


class Entry(models.Model): # Écriture en Français
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    ref_date = models.DateField('transaction date')
    explanation = models.CharField(max_length=200) # libellé en Français

    def __str__(self):
        return "{0} {1}".format(self.ref_date, self.explanation)


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

    def __str__(self):
        if self.is_debit():
            message = "{0} | {1} | -"
        else:
            message = "{0} | - | {1}"
        return message.format(self.account, self.amount)
