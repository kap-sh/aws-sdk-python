"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobRefreshScheduleOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

AssetBundleImportJobRefreshScheduleOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.AssetBundleImportJobRefreshScheduleOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobRefreshScheduleOverrideParametersList,
) -> list:
    import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobRefreshScheduleOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

    out: AssetBundleImportJobRefreshScheduleOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.deserialize_json(
                item
            )
        )
    return out
