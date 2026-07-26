"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobWarningList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_warning

AssetBundleExportJobWarningList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_warning.AssetBundleExportJobWarning"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobWarningList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_warning

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_warning.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobWarningList:
    import capo_quicksight.types.asset_bundle_export_job_warning

    out: AssetBundleExportJobWarningList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_warning.deserialize_json(item)
        )
    return out
