"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions

AssetBundleImportJobDataSourceOverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions.AssetBundleImportJobDataSourceOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobDataSourceOverridePermissionsList,
) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobDataSourceOverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions

    out: AssetBundleImportJobDataSourceOverridePermissionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_permissions.deserialize_json(
                item
            )
        )
    return out
