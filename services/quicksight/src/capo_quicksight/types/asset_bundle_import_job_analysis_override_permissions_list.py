"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions

AssetBundleImportJobAnalysisOverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions.AssetBundleImportJobAnalysisOverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverridePermissionsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobAnalysisOverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions

    out: AssetBundleImportJobAnalysisOverridePermissionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_analysis_override_permissions.deserialize_json(
                item
            )
        )
    return out
