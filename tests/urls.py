""" Url router for the main application
"""
from django.conf.urls import include
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from core_main_app.components.blob import api as blob_api
from core_main_app.components.data import api as data_api
from core_main_app.utils.rendering import render
from core_main_app.views.common import (
    ajax as common_ajax,
    views as common_views,
)
from core_main_app.views.user import views as user_views, ajax as user_ajax

get_schema_view(
    openapi.Info(
        title="REST API",
        default_version="v1",
    ),
)

urlpatterns = [
    re_path(r"^$", user_views.homepage, name="core_main_app_homepage"),
    re_path(r"^login", user_views.custom_login, name="core_main_app_login"),
    re_path(r"^rest/", include("tests.rest_urls")),
    re_path(
        r"^data",
        common_views.ViewData.as_view(),
        name="core_main_app_data_detail",
    ),
    re_path(
        r"^template/versions/(?P<version_manager_id>\w+)",
        user_views.manage_template_versions,
        name="core_main_app_manage_template_versions",
    ),
    re_path(
        r"^template/(?P<pk>[\w-]+)/edit/$",
        common_ajax.EditTemplateVersionManagerView.as_view(),
        name="core_main_app_edit_template",
    ),
    re_path(
        r"^template/xslt/(?P<template_id>\w+)",
        common_views.TemplateXSLRenderingView.as_view(
            rendering=render,
            template_name="core_main_app/common/templates_xslt/main.html",
            save_redirect="core_main_app_manage_template_versions",
        ),
        name="core_main_app_template_xslt",
    ),
    re_path(
        r"^edit-rights/(?P<workspace_id>\w+)$",
        common_views.EditWorkspaceRights.as_view(),
        name="core_main_edit_rights_workspace",
    ),
    re_path(
        r"^change-workspace",
        user_ajax.LoadFormChangeWorkspace.as_view(),
        name="core_main_change_workspace",
    ),
    re_path(
        r"^assign-blob-workspace",
        user_ajax.AssignView.as_view(api=blob_api),
        name="core_main_assign_blob_workspace",
    ),
    re_path(
        r"^assign-data-workspace",
        user_ajax.AssignView.as_view(api=data_api),
        name="core_main_assign_data_workspace",
    ),
    re_path(
        r"^add-user-form",
        user_ajax.load_add_user_form,
        name="core_main_edit_rights_users_form",
    ),
    re_path(
        r"^add-user-right-to-workspace",
        user_ajax.add_user_right_to_workspace,
        name="core_main_add_user_right_to_workspace",
    ),
    re_path(
        r"^switch-right", user_ajax.switch_right, name="core_main_switch_right"
    ),
    re_path(
        r"^remove-rights",
        user_ajax.remove_user_or_group_rights,
        name="core_main_remove_rights",
    ),
    re_path(
        r"^add-group-form",
        user_ajax.load_add_group_form,
        name="core_main_edit_rights_groups_form",
    ),
    re_path(
        r"^add-group-right-to-workspace",
        user_ajax.add_group_right_to_workspace,
        name="core_main_add_group_right_to_workspace",
    ),
    re_path(r"^tz_detect/", include("tz_detect.urls")),
    re_path(
        r"^change-data-display",
        user_ajax.change_data_display,
        name="core_main_add_change_data_display",
    ),
    re_path(
        r"^redirect-record",
        user_ajax.change_data_display,
        name="core_dashboard_records",
    ),
]
