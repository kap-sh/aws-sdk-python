"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobFolderOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_folder_override_properties

AssetBundleExportJobFolderOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_folder_override_properties.AssetBundleExportJobFolderOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobFolderOverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_folder_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_folder_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobFolderOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_folder_override_properties

    out: AssetBundleExportJobFolderOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_folder_override_properties.deserialize_json(
                item
            )
        )
    return out
