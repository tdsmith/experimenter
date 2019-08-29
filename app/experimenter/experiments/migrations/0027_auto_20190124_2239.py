# Generated by Django 2.1.2 on 2019-01-24 22:39
import datetime
from django.db import migrations, models


def set_durations(apps, schema_editor):  # pragma: no cover
    Experiment = apps.get_model("experiments", "Experiment")

    for experiment in Experiment.objects.all():
        if experiment.proposed_start_date and experiment.proposed_end_date:
            new_duration = (
                experiment.proposed_end_date - experiment.proposed_start_date
            ).days
            if new_duration > 0:
                experiment.proposed_duration = new_duration
                experiment.save()


def set_end_dates(apps, schema_editor):  # pragma: no cover
    Experiment = apps.get_model("experiments", "Experiment")

    for experiment in Experiment.objects.all():
        if experiment.proposed_start_date and experiment.proposed_duration:
            experiment.proposed_end_date = (
                experiment.proposed_start_date
                + datetime.timedelta(days=experiment.proposed_duration)
            )
            experiment.save()


class Migration(migrations.Migration):

    dependencies = [("experiments", "0026_auto_20190110_2103")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="proposed_duration",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experiment",
            name="proposed_enrollment",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.RunPython(set_durations, set_end_dates),
        migrations.RemoveField(model_name="experiment", name="proposed_end_date"),
        migrations.AlterField(
            model_name="experiment",
            name="risks",
            field=models.TextField(
                blank=True,
                default="If you answered “yes” to any of the above, your study is considered High Risk\nand needs executive sponsor sign-off.\n\nPlease state the known risk(s) here and any mitigation(s).\n\nFor a high risk study, each of the following must be provided\nand accounted for:\n\nFinal Experiment Design\n    Responsible: Experiment owner\n    Accountable: Data Scientist\n\nData Analysis\n    Responsible: Assigned analyst\n    Accountable: Experiment owner / PM\n\nLegal Sign-\n    Off Responsible: Experiment owner\n    Accountable: PM and/or EPM\n\nShipping\n    Responsible: Experiment owner\n    Accountable: Release Mgmt\n\nRisk Matrix\n    Responsible: Experiment owner\n    Accountable: Product Manager",
                null=True,
            ),
        ),
    ]
