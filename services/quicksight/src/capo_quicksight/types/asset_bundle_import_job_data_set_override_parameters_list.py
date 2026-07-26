"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters

AssetBundleImportJobDataSetOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters.AssetBundleImportJobDataSetOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDataSetOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters

    out: AssetBundleImportJobDataSetOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters.deserialize_json(
                item
            )
        )
    return out
