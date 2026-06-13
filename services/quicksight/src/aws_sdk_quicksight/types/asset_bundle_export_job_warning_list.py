"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobWarningList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_warning

AssetBundleExportJobWarningList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_warning.AssetBundleExportJobWarning"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobWarningList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_warning

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_warning.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobWarningList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_warning

    out: AssetBundleExportJobWarningList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_warning.deserialize_json(
                item
            )
        )
    return out
