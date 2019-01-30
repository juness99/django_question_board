from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    #host가없는 댓글은 존재하지가 않는다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#어떤정보를 가져올지 (부모역할)
    content = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.content