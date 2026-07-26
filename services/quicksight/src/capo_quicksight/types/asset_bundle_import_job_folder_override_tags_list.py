"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobFolderOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_tags

AssetBundleImportJobFolderOverrideTagsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_folder_override_tags.AssetBundleImportJobFolderOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobFolderOverrideTagsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_tags

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_folder_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobFolderOverrideTagsList:
    import capo_quicksight.types.asset_bundle_import_job_folder_override_tags

    out: AssetBundleImportJobFolderOverrideTagsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_folder_override_tags.deserialize_json(
                item
            )
        )
    return out
