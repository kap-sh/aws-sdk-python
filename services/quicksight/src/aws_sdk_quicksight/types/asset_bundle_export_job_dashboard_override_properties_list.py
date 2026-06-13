"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties

AssetBundleExportJobDashboardOverridePropertiesList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties.AssetBundleExportJobDashboardOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDashboardOverridePropertiesList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobDashboardOverridePropertiesList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties

    out: AssetBundleExportJobDashboardOverridePropertiesList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_dashboard_override_properties.deserialize_json(
                item
            )
        )
    return out
