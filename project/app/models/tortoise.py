from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    """
    Define a new database model called TextSummary.
    """

    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)
