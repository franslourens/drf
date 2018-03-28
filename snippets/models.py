from django.db import models
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    #highlighted = models.TextField()

    class Meta:
        ordering = ('created',)
        
    @staticmethod
    def all(test):
        count = 0
        while (count < 9):
           print 'The count is:', count
           count = count + 1
        
        print "Good bye!"
        return True
    
    def validation(self):
        """
        Validation
        
        Validate manditory fields for content
        """
        manditory_fields  = ["title","code"]
        attributes = self.serialize()
        
        errors = []
        
        for field in manditory_fields:
            if not attributes[field]: 
                errors.append("{0} must be assigned a value".format(field))
    
        if len(errors):
            raise ValidationError("Content is not valid: {0}".format(errors))
        
        return True
    
    def serialize(self, ):
        return {
            "created" : str(self.created),
            "title" : str(self.title),
            "code" : str(self.code),
            "linenos" : str(self.linenos),
            "language" : str(self.language),
            "style" : str(self.style),
         }      