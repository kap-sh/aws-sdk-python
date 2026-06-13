"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobOverrideParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list


class AssetBundleImportJobOverrideParameters(TypedDict):
    resource_id_override_configuration: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.AssetBundleImportJobResourceIdOverrideConfiguration"
    ]
    """<p>An optional structure that configures resource ID overrides to be applied within the import job.</p>"""
    vpc_connections: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.AssetBundleImportJobVPCConnectionOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>VPCConnection</code> resources that are present in the asset bundle that is imported.</p>"""
    refresh_schedules: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.AssetBundleImportJobRefreshScheduleOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>RefreshSchedule</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sources: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.AssetBundleImportJobDataSourceOverrideParametersList"
    ]
    """<p> A list of overrides for any <code>DataSource</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sets: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.AssetBundleImportJobDataSetOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>DataSet</code> resources that are present in the asset bundle that is imported.</p>"""
    themes: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.AssetBundleImportJobThemeOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Theme</code> resources that are present in the asset bundle that is imported.</p>"""
    analyses: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.AssetBundleImportJobAnalysisOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Analysis</code> resources that are present in the asset bundle that is imported.</p>"""
    dashboards: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.AssetBundleImportJobDashboardOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Dashboard</code> resources that are present in the asset bundle that is imported.</p>"""
    folders: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.AssetBundleImportJobFolderOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Folder</code> resources that are present in the asset bundle that is imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobOverrideParameters) -> dict:
    out: dict = {}
    if "resource_id_override_configuration" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration

        out["ResourceIdOverrideConfiguration"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.serialize_json(
                value["resource_id_override_configuration"]
            )
        )
    if "vpc_connections" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list

        out["VPCConnections"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.serialize_json(
                value["vpc_connections"]
            )
        )
    if "refresh_schedules" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list

        out["RefreshSchedules"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "data_sources" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list

        out["DataSources"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.serialize_json(
                value["data_sources"]
            )
        )
    if "data_sets" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list

        out["DataSets"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.serialize_json(
                value["data_sets"]
            )
        )
    if "themes" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list

        out["Themes"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.serialize_json(
                value["themes"]
            )
        )
    if "analyses" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list

        out["Analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.serialize_json(
                value["analyses"]
            )
        )
    if "dashboards" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list

        out["Dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.serialize_json(
                value["dashboards"]
            )
        )
    if "folders" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list

        out["Folders"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.serialize_json(
                value["folders"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobOverrideParameters:
    out: AssetBundleImportJobOverrideParameters = {}  # type: ignore[typeddict-item]
    if "ResourceIdOverrideConfiguration" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration

        out["resource_id_override_configuration"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.deserialize_json(
                data["ResourceIdOverrideConfiguration"]
            )
        )
    if "VPCConnections" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list

        out["vpc_connections"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.deserialize_json(
                data["VPCConnections"]
            )
        )
    if "RefreshSchedules" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list

        out["refresh_schedules"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if "DataSources" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list

        out["data_sources"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.deserialize_json(
                data["DataSources"]
            )
        )
    if "DataSets" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list

        out["data_sets"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.deserialize_json(
                data["DataSets"]
            )
        )
    if "Themes" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list

        out["themes"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.deserialize_json(
                data["Themes"]
            )
        )
    if "Analyses" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list

        out["analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.deserialize_json(
                data["Analyses"]
            )
        )
    if "Dashboards" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list

        out["dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.deserialize_json(
                data["Dashboards"]
            )
        )
    if "Folders" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list

        out["folders"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.deserialize_json(
                data["Folders"]
            )
        )
    return out
