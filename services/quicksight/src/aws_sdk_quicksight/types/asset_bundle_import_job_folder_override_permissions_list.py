"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobFolderOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions

AssetBundleImportJobFolderOverridePermissionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions.AssetBundleImportJobFolderOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobFolderOverridePermissionsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobFolderOverridePermissionsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions

    out: AssetBundleImportJobFolderOverridePermissionsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_folder_override_permissions.deserialize_json(
                item
            )
        )
    return out
