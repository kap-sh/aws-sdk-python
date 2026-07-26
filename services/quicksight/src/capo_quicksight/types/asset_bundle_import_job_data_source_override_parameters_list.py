"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

AssetBundleImportJobDataSourceOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.AssetBundleImportJobDataSourceOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobDataSourceOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

    out: AssetBundleImportJobDataSourceOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.deserialize_json(
                item
            )
        )
    return out
