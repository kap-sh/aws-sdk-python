"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags

AssetBundleImportJobDataSetOverrideTagsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags.AssetBundleImportJobDataSetOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideTagsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDataSetOverrideTagsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags

    out: AssetBundleImportJobDataSetOverrideTagsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_data_set_override_tags.deserialize_json(
                item
            )
        )
    return out
