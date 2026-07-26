"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

AssetBundleImportJobDashboardOverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.AssetBundleImportJobDashboardOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverridePermissionsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobDashboardOverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

    out: AssetBundleImportJobDashboardOverridePermissionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.deserialize_json(
                item
            )
        )
    return out
