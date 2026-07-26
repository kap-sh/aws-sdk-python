"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobWarningList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_warning

AssetBundleImportJobWarningList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_warning.AssetBundleImportJobWarning"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobWarningList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_warning

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_warning.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobWarningList:
    import capo_quicksight.types.asset_bundle_import_job_warning

    out: AssetBundleImportJobWarningList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_warning.deserialize_json(item)
        )
    return out
