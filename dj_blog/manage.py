from django.db import models

#create yours models here.
class Category(models.Model):
    tittle = models.CharField(max_length=255)

    class Meta:
        ordering = ('title')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tittle
   
    class post(models.Mode):

        ACTIVE= 'active'
        DRAFT= 'draft'

        CHOICES_STATUS = {
            (ACTIVE, 'active'),
            (DRAFT, 'draft')
        }

        Category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        intro = models.TextField()
        body = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
        image = models.ImageField(upload_to='upload/', blank=True, null=True)

        def __str__(self):
            return self.title
       
    class Comment (models.Mode):
        post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
      
  email = models.EmailField()
        body = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
