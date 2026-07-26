"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardPropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override

AssetBundleExportJobDashboardPropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override.AssetBundleExportJobDashboardPropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDashboardPropertyToOverrideList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobDashboardPropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override

    out: AssetBundleExportJobDashboardPropertyToOverrideList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override.deserialize_json(
                item
            )
        )
    return out
