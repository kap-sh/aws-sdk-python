"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list


class AssetBundleImportJobOverrideTags(TypedDict, closed=True):
    vpc_connections: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list.AssetBundleImportJobVPCConnectionOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>VPCConnection</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sources: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list.AssetBundleImportJobDataSourceOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>DataSource</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sets: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list.AssetBundleImportJobDataSetOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>DataSet</code> resources that are present in the asset bundle that is imported.</p>"""
    themes: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list.AssetBundleImportJobThemeOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>Theme</code> resources that are present in the asset bundle that is imported.</p>"""
    analyses: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list.AssetBundleImportJobAnalysisOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>Analysis</code> resources that are present in the asset bundle that is imported.</p>"""
    dashboards: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list.AssetBundleImportJobDashboardOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>Dashboard</code> resources that are present in the asset bundle that is imported.</p>"""
    folders: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list.AssetBundleImportJobFolderOverrideTagsList"
    ]
    """<p>A list of tag overrides for any <code>Folder</code> resources that are present in the asset bundle that is imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobOverrideTags) -> dict:
    out: dict = {}
    if "vpc_connections" in value:
        import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list

        out["VPCConnections"] = (
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list.serialize_json(
                value["vpc_connections"]
            )
        )
    if "data_sources" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list

        out["DataSources"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list.serialize_json(
                value["data_sources"]
            )
        )
    if "data_sets" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list

        out["DataSets"] = (
            capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list.serialize_json(
                value["data_sets"]
            )
        )
    if "themes" in value:
        import capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list

        out["Themes"] = (
            capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list.serialize_json(
                value["themes"]
            )
        )
    if "analyses" in value:
        import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list

        out["Analyses"] = (
            capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list.serialize_json(
                value["analyses"]
            )
        )
    if "dashboards" in value:
        import capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list

        out["Dashboards"] = (
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list.serialize_json(
                value["dashboards"]
            )
        )
    if "folders" in value:
        import capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list

        out["Folders"] = (
            capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list.serialize_json(
                value["folders"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobOverrideTags:
    out: AssetBundleImportJobOverrideTags = {}  # type: ignore[typeddict-item]
    if "VPCConnections" in data:
        import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list

        out["vpc_connections"] = (
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags_list.deserialize_json(
                data["VPCConnections"]
            )
        )
    if "DataSources" in data:
        import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list

        out["data_sources"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_override_tags_list.deserialize_json(
                data["DataSources"]
            )
        )
    if "DataSets" in data:
        import capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list

        out["data_sets"] = (
            capo_quicksight.types.asset_bundle_import_job_data_set_override_tags_list.deserialize_json(
                data["DataSets"]
            )
        )
    if "Themes" in data:
        import capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list

        out["themes"] = (
            capo_quicksight.types.asset_bundle_import_job_theme_override_tags_list.deserialize_json(
                data["Themes"]
            )
        )
    if "Analyses" in data:
        import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list

        out["analyses"] = (
            capo_quicksight.types.asset_bundle_import_job_analysis_override_tags_list.deserialize_json(
                data["Analyses"]
            )
        )
    if "Dashboards" in data:
        import capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list

        out["dashboards"] = (
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_tags_list.deserialize_json(
                data["Dashboards"]
            )
        )
    if "Folders" in data:
        import capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list

        out["folders"] = (
            capo_quicksight.types.asset_bundle_import_job_folder_override_tags_list.deserialize_json(
                data["Folders"]
            )
        )
    return out
