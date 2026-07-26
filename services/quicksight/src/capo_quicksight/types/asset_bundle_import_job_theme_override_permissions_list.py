"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_theme_override_permissions

AssetBundleImportJobThemeOverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_theme_override_permissions.AssetBundleImportJobThemeOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverridePermissionsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_theme_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_theme_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobThemeOverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_theme_override_permissions

    out: AssetBundleImportJobThemeOverridePermissionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_theme_override_permissions.deserialize_json(
                item
            )
        )
    return out
