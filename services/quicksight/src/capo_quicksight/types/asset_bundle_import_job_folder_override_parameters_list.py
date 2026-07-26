"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobFolderOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters

AssetBundleImportJobFolderOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_folder_override_parameters.AssetBundleImportJobFolderOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobFolderOverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_folder_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobFolderOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters

    out: AssetBundleImportJobFolderOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_folder_override_parameters.deserialize_json(
                item
            )
        )
    return out
