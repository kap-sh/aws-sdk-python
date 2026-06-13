"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

AssetBundleImportJobDashboardOverridePermissionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.AssetBundleImportJobDashboardOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverridePermissionsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobDashboardOverridePermissionsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions

    out: AssetBundleImportJobDashboardOverridePermissionsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_permissions.deserialize_json(
                item
            )
        )
    return out
