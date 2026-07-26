"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_error

AssetBundleImportJobErrorList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_error.AssetBundleImportJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobErrorList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_error

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobErrorList:
    import capo_quicksight.types.asset_bundle_import_job_error

    out: AssetBundleImportJobErrorList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_error.deserialize_json(item)
        )
    return out
