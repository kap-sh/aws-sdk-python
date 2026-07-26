"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions

AssetBundleImportJobDataSetOverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions.AssetBundleImportJobDataSetOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverridePermissionsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDataSetOverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions

    out: AssetBundleImportJobDataSetOverridePermissionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_set_override_permissions.deserialize_json(
                item
            )
        )
    return out
