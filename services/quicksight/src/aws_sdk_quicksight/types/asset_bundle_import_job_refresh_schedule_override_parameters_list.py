"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobRefreshScheduleOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

AssetBundleImportJobRefreshScheduleOverrideParametersList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.AssetBundleImportJobRefreshScheduleOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobRefreshScheduleOverrideParametersList,
) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobRefreshScheduleOverrideParametersList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters

    out: AssetBundleImportJobRefreshScheduleOverrideParametersList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters.deserialize_json(
                item
            )
        )
    return out
