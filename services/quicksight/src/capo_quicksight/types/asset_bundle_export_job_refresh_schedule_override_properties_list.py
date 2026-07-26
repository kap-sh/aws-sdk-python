"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshScheduleOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties

AssetBundleExportJobRefreshScheduleOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties.AssetBundleExportJobRefreshScheduleOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobRefreshScheduleOverridePropertiesList,
) -> list:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobRefreshScheduleOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties

    out: AssetBundleExportJobRefreshScheduleOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_refresh_schedule_override_properties.deserialize_json(
                item
            )
        )
    return out
