# Generated by Django 5.0.1 on 2024-02-02 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0002_remove_book_isbn_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='purchase_date',
        ),
    ]
