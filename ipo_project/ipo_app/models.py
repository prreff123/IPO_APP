from django.db import models

class IPO(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Closed', 'Closed'),
        ('Listed', 'Listed'),
        ('Ongoing', 'Ongoing'),
    ]

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
    rhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.company_name

