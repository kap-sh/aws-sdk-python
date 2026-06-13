"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobThemePropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override

AssetBundleExportJobThemePropertyToOverrideList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override.AssetBundleExportJobThemePropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobThemePropertyToOverrideList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobThemePropertyToOverrideList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override

    out: AssetBundleExportJobThemePropertyToOverrideList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override.deserialize_json(
                item
            )
        )
    return out
