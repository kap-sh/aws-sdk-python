"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_summary

AssetBundleExportJobSummaryList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_summary.AssetBundleExportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobSummaryList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobSummaryList:
    import capo_quicksight.types.asset_bundle_export_job_summary

    out: AssetBundleExportJobSummaryList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_summary.deserialize_json(item)
        )
    return out
