"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_summary

AssetBundleImportJobSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_summary.AssetBundleImportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobSummaryList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobSummaryList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_summary

    out: AssetBundleImportJobSummaryList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_summary.deserialize_json(
                item
            )
        )
    return out
