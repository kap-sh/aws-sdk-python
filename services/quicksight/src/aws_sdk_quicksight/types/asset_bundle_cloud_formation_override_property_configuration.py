"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleCloudFormationOverridePropertyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list


class AssetBundleCloudFormationOverridePropertyConfiguration(TypedDict):
    resource_id_override_configuration: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration.AssetBundleExportJobResourceIdOverrideConfiguration"
    ]
    """<p>An optional list of structures that control how resource IDs are parameterized in the returned CloudFormation template.</p>"""
    vpc_connections: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list.AssetBundleExportJobVPCConnectionOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>VPCConnection</code> resources are parameterized in the returned CloudFormation template.</p>"""
    refresh_schedules: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list.AssetBundleExportJobRefreshScheduleOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>RefreshSchedule</code> resources are parameterized in the returned CloudFormation template.</p>"""
    data_sources: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list.AssetBundleExportJobDataSourceOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>DataSource</code> resources are parameterized in the returned CloudFormation template.</p>"""
    data_sets: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list.AssetBundleExportJobDataSetOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>DataSet</code> resources are parameterized in the returned CloudFormation template.</p>"""
    themes: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list.AssetBundleExportJobThemeOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>Theme</code> resources are parameterized in the returned CloudFormation template.</p>"""
    analyses: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list.AssetBundleExportJobAnalysisOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>Analysis</code> resources are parameterized in the returned CloudFormation template.</p>"""
    dashboards: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list.AssetBundleExportJobDashboardOverridePropertiesList"
    ]
    """<p>An optional list of structures that control how <code>Dashboard</code> resources are parameterized in the returned CloudFormation template.</p>"""
    folders: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list.AssetBundleExportJobFolderOverridePropertiesList"
    ]
    """<p>An optional list of structures that controls how <code>Folder</code> resources are parameterized in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleCloudFormationOverridePropertyConfiguration,
) -> dict:
    out: dict = {}
    if "resource_id_override_configuration" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration

        out["ResourceIdOverrideConfiguration"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration.serialize_json(
                value["resource_id_override_configuration"]
            )
        )
    if "vpc_connections" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list

        out["VPCConnections"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list.serialize_json(
                value["vpc_connections"]
            )
        )
    if "refresh_schedules" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list

        out["RefreshSchedules"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "data_sources" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list

        out["DataSources"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list.serialize_json(
                value["data_sources"]
            )
        )
    if "data_sets" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list

        out["DataSets"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list.serialize_json(
                value["data_sets"]
            )
        )
    if "themes" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list

        out["Themes"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list.serialize_json(
                value["themes"]
            )
        )
    if "analyses" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list

        out["Analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list.serialize_json(
                value["analyses"]
            )
        )
    if "dashboards" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list

        out["Dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list.serialize_json(
                value["dashboards"]
            )
        )
    if "folders" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list

        out["Folders"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list.serialize_json(
                value["folders"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AssetBundleCloudFormationOverridePropertyConfiguration:
    out: AssetBundleCloudFormationOverridePropertyConfiguration = {}  # type: ignore[typeddict-item]
    if "ResourceIdOverrideConfiguration" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration

        out["resource_id_override_configuration"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_resource_id_override_configuration.deserialize_json(
                data["ResourceIdOverrideConfiguration"]
            )
        )
    if "VPCConnections" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list

        out["vpc_connections"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties_list.deserialize_json(
                data["VPCConnections"]
            )
        )
    if "RefreshSchedules" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list

        out["refresh_schedules"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties_list.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if "DataSources" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list

        out["data_sources"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties_list.deserialize_json(
                data["DataSources"]
            )
        )
    if "DataSets" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list

        out["data_sets"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_data_set_override_properties_list.deserialize_json(
                data["DataSets"]
            )
        )
    if "Themes" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list

        out["themes"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_theme_override_properties_list.deserialize_json(
                data["Themes"]
            )
        )
    if "Analyses" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list

        out["analyses"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_analysis_override_properties_list.deserialize_json(
                data["Analyses"]
            )
        )
    if "Dashboards" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list

        out["dashboards"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties_list.deserialize_json(
                data["Dashboards"]
            )
        )
    if "Folders" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list

        out["folders"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties_list.deserialize_json(
                data["Folders"]
            )
        )
    return out
