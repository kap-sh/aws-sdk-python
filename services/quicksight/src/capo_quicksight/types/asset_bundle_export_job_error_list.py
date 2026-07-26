"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_error

AssetBundleExportJobErrorList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_error.AssetBundleExportJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobErrorList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_error

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobErrorList:
    import capo_quicksight.types.asset_bundle_export_job_error

    out: AssetBundleExportJobErrorList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_error.deserialize_json(item)
        )
    return out
