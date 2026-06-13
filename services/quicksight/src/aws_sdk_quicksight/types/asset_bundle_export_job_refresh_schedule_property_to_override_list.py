"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshSchedulePropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

AssetBundleExportJobRefreshSchedulePropertyToOverrideList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.AssetBundleExportJobRefreshSchedulePropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobRefreshSchedulePropertyToOverrideList,
) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobRefreshSchedulePropertyToOverrideList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

    out: AssetBundleExportJobRefreshSchedulePropertyToOverrideList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.deserialize_json(
                item
            )
        )
    return out
