# Generated by Django 4.0.5 on 2022-06-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_cake_flavours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='flavours',
            field=models.CharField(choices=[('#f4f0d2', 'Plain Sponge'), ('#e8b26b', 'Caramel'), ('#543e28', 'Chocolate'), ('#fff3c9', 'Cream Cheese'), ('#fad2e6', 'Fruit'), ('#d48c55', 'Spiced'), ('#fffeeb', 'Vanilla'), ('#f1b0ff', 'Experimental')], default='#f4f0d2', max_length=7),
        ),
    ]
