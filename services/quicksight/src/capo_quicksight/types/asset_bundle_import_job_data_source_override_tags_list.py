"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags

AssetBundleImportJobDataSourceOverrideTagsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_source_override_tags.AssetBundleImportJobDataSourceOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideTagsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDataSourceOverrideTagsList:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_tags

    out: AssetBundleImportJobDataSourceOverrideTagsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_tags.deserialize_json(
                item
            )
        )
    return out
