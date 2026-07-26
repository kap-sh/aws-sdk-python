"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshSchedulePropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

AssetBundleExportJobRefreshSchedulePropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.AssetBundleExportJobRefreshSchedulePropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobRefreshSchedulePropertyToOverrideList,
) -> list:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobRefreshSchedulePropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override

    out: AssetBundleExportJobRefreshSchedulePropertyToOverrideList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override.deserialize_json(
                item
            )
        )
    return out
