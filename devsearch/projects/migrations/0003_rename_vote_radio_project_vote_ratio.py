# Generated by Django 4.2.7 on 2023-11-20 15:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_tag_project_vote_radio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="vote_radio",
            new_name="vote_ratio",
        ),
    ]