"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobFolderOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties

AssetBundleExportJobFolderOverridePropertiesList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties.AssetBundleExportJobFolderOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobFolderOverridePropertiesList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobFolderOverridePropertiesList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties

    out: AssetBundleExportJobFolderOverridePropertiesList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_folder_override_properties.deserialize_json(
                item
            )
        )
    return out
