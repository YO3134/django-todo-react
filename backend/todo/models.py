from django.db import models
# vscode にて仮想環境の認識errorが表示される場合有


class Todo(models.Model):  # add this
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
