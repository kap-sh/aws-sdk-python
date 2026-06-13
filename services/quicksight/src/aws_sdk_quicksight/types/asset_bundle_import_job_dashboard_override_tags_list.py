"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags

AssetBundleImportJobDashboardOverrideTagsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags.AssetBundleImportJobDashboardOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverrideTagsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDashboardOverrideTagsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags

    out: AssetBundleImportJobDashboardOverrideTagsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_dashboard_override_tags.deserialize_json(
                item
            )
        )
    return out
