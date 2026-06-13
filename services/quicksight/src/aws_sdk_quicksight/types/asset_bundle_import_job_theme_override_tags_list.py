"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags

AssetBundleImportJobThemeOverrideTagsList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags.AssetBundleImportJobThemeOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverrideTagsList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobThemeOverrideTagsList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags

    out: AssetBundleImportJobThemeOverrideTagsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_tags.deserialize_json(
                item
            )
        )
    return out
