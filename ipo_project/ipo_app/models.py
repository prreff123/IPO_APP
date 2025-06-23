from django.db import models
from datetime import date
class IPO(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Closed', 'Closed'),
        ('Listed', 'Listed'),
        ('Ongoing', 'Ongoing'),
    ]

    def auto_update_status(self):
        today = date.today()
        if today < self.opening_date:
            self.status = 'Upcoming'
        elif self.opening_date <= today <= self.closing_date:
            self.status = 'Ongoing'
        elif today > self.closing_date and today < self.listing_date:
            self.status = 'Closed'
        elif today >= self.listing_date:
            self.status = 'Listed'
        self.save()

    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    price_band = models.CharField(max_length=50)
    opening_date = models.DateField()
    closing_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    listing_gain = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_return = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rhp_pdf = models.FileField(upload_to='pdfs/rhp/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='pdfs/drhp/', null=True, blank=True)

    def __str__(self):
        return self.company_name

