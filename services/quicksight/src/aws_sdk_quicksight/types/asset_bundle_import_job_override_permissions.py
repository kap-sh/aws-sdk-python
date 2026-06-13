"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobOverridePermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list


class AssetBundleImportJobOverridePermissions(TypedDict):
    data_sources: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list.AssetBundleImportJobDataSourceOverridePermissionsList"
    ]
    """<p>A list of permissions overrides for any <code>DataSource</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sets: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list.AssetBundleImportJobDataSetOverridePermissionsList"
    ]
    """<p>A list of permissions overrides for any <code>DataSet</code> resources that are present in the asset bundle that is imported.</p>"""
    themes: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list.AssetBundleImportJobThemeOverridePermissionsList"
    ]
    """<p>A list of permissions overrides for any <code>Theme</code> resources that are present in the asset bundle that is imported.</p>"""
    analyses: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list.AssetBundleImportJobAnalysisOverridePermissionsList"
    ]
    """<p>A list of permissions overrides for any <code>Analysis</code> resources that are present in the asset bundle that is imported.</p>"""
    dashboards: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list.AssetBundleImportJobDashboardOverridePermissionsList"
    ]
    """<p>A list of permissions overrides for any <code>Dashboard</code> resources that are present in the asset bundle that is imported.</p>"""
    folders: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list.AssetBundleImportJobFolderOverridePermissionsList"
    ]
    """<p>A list of permissions for the folders that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobOverridePermissions) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list

        out["DataSources"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list.serialize_json(
                value["data_sources"]
            )
        )
    if "data_sets" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list

        out["DataSets"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list.serialize_json(
                value["data_sets"]
            )
        )
    if "themes" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list

        out["Themes"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list.serialize_json(
                value["themes"]
            )
        )
    if "analyses" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list

        out["Analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list.serialize_json(
                value["analyses"]
            )
        )
    if "dashboards" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list

        out["Dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list.serialize_json(
                value["dashboards"]
            )
        )
    if "folders" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list

        out["Folders"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list.serialize_json(
                value["folders"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobOverridePermissions:
    out: AssetBundleImportJobOverridePermissions = {}  # type: ignore[typeddict-item]
    if "DataSources" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list

        out["data_sources"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_permissions_list.deserialize_json(
                data["DataSources"]
            )
        )
    if "DataSets" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list

        out["data_sets"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions_list.deserialize_json(
                data["DataSets"]
            )
        )
    if "Themes" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list

        out["themes"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_permissions_list.deserialize_json(
                data["Themes"]
            )
        )
    if "Analyses" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list

        out["analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_permissions_list.deserialize_json(
                data["Analyses"]
            )
        )
    if "Dashboards" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list

        out["dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions_list.deserialize_json(
                data["Dashboards"]
            )
        )
    if "Folders" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list

        out["folders"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions_list.deserialize_json(
                data["Folders"]
            )
        )
    return out
