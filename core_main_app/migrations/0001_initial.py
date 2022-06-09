# Generated by Django 3.2 on 2021-12-02 01:51

import core_main_app.components.blob.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

from core_main_app.settings import XSD_UPLOAD_DIR, XSLT_UPLOAD_DIR


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dict_content", models.JSONField(blank=True, null=True)),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                (
                    "xml_file",
                    models.FileField(
                        max_length=250,
                        upload_to=core_main_app.utils.storage.storage.user_directory_path,
                    ),
                ),
                (
                    "checksum",
                    models.CharField(
                        blank=True, default=None, max_length=512, null=True
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "last_modification_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "last_change_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("user_id", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Data",
                "verbose_name_plural": "Data",
            },
        ),
        migrations.CreateModel(
            name="Main",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "core_main_app",
                "permissions": (
                    ("publish_data", "Can publish data"),
                    ("publish_blob", "Can publish blob"),
                ),
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_current", models.BooleanField(default=False)),
                ("is_disabled", models.BooleanField(default=False)),
                (
                    "filename",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                (
                    "file",
                    models.FileField(max_length=250, upload_to=XSD_UPLOAD_DIR),
                ),
                (
                    "checksum",
                    models.CharField(
                        blank=True, default=None, max_length=512, null=True
                    ),
                ),
                (
                    "user",
                    models.CharField(
                        blank=True, default=None, max_length=200, null=True
                    ),
                ),
                ("hash", models.CharField(max_length=200)),
                ("_display_name", models.CharField(blank=True, max_length=200)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("_cls", models.CharField(default="Template", max_length=200)),
                (
                    "dependencies",
                    models.ManyToManyField(
                        blank=True,
                        default=[],
                        related_name="_core_main_app_template_dependencies_+",
                        to="core_main_app.Template",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TemplateVersionManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                (
                    "user",
                    models.CharField(
                        blank=True, default=None, max_length=200, null=True
                    ),
                ),
                ("is_disabled", models.BooleanField(default=False)),
                ("_cls", models.CharField(default="VersionManager", max_length=200)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.IntegerField()),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Workspace",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                ("owner", models.CharField(blank=True, max_length=200, null=True)),
                ("read_perm_id", models.CharField(max_length=200)),
                ("write_perm_id", models.CharField(max_length=200)),
                ("is_public", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="XslTransformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        unique=True,
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                (
                    "filename",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                (
                    "file",
                    models.FileField(max_length=250, upload_to=XSLT_UPLOAD_DIR),
                ),
                (
                    "checksum",
                    models.CharField(
                        blank=True, default=None, max_length=512, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TemplateXslRendering",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "default_detail_xslt",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="default_detail_xslt",
                        to="core_main_app.xsltransformation",
                    ),
                ),
                (
                    "list_detail_xslt",
                    models.ManyToManyField(
                        blank=True, default=[], to="core_main_app.XslTransformation"
                    ),
                ),
                (
                    "list_xslt",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="list_xslt",
                        to="core_main_app.xsltransformation",
                    ),
                ),
                (
                    "template",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_main_app.template",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="template",
            name="version_manager",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core_main_app.templateversionmanager",
            ),
        ),
        migrations.CreateModel(
            name="DatabaseLockObject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=200)),
                ("lock_date", models.DateTimeField()),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_main_app.data",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="data",
            name="template",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core_main_app.template"
            ),
        ),
        migrations.AddField(
            model_name="data",
            name="workspace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core_main_app.workspace",
            ),
        ),
        migrations.CreateModel(
            name="Blob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "filename",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Filename must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                ("user_id", models.CharField(max_length=200)),
                (
                    "blob",
                    models.FileField(
                        null=True,
                        max_length=250,
                        upload_to=core_main_app.utils.storage.storage.user_directory_path,
                    ),
                ),
                (
                    "checksum",
                    models.CharField(
                        blank=True, default=None, max_length=512, null=True
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "workspace",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core_main_app.workspace",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="data",
            index=models.Index(
                fields=["title", "last_modification_date", "template", "user_id"],
                name="core_main_a_title_3e9383_idx",
            ),
        ),
    ]
