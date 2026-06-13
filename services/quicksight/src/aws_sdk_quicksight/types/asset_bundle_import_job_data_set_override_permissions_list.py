"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions

AssetBundleImportJobDataSetOverridePermissionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions.AssetBundleImportJobDataSetOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverridePermissionsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDataSetOverridePermissionsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions

    out: AssetBundleImportJobDataSetOverridePermissionsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_permissions.deserialize_json(
                item
            )
        )
    return out
