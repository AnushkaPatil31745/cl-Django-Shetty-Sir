from django.db import models
#  Copy Code from https://docs.djangoproject.com/en/3.1/topics/db/queries/

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return '%s --%s' % (self.name, self.tagline)

     # def __str__(self):
     #    return '%s -- %s --%d' % (self.name, self.country, self.population)
    

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline



    # Blog : ['name','tagline']

    # Author : ['name','email']

    # Entry : ['blog','headline','body_text','pub_date','mod_date',
    # 'authors','number_of_comments','number_of_pingbacks']    