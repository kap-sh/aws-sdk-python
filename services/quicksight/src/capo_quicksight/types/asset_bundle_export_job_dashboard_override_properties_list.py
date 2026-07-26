"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties

AssetBundleExportJobDashboardOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties.AssetBundleExportJobDashboardOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDashboardOverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobDashboardOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties

    out: AssetBundleExportJobDashboardOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_dashboard_override_properties.deserialize_json(
                item
            )
        )
    return out
