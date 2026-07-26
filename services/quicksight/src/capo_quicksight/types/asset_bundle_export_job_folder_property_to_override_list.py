"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobFolderPropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_folder_property_to_override

AssetBundleExportJobFolderPropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_folder_property_to_override.AssetBundleExportJobFolderPropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobFolderPropertyToOverrideList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_folder_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_folder_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobFolderPropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_folder_property_to_override

    out: AssetBundleExportJobFolderPropertyToOverrideList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_folder_property_to_override.deserialize_json(
                item
            )
        )
    return out
