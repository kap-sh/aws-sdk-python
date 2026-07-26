"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobThemeOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_theme_override_properties

AssetBundleExportJobThemeOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_theme_override_properties.AssetBundleExportJobThemeOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobThemeOverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_theme_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_theme_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobThemeOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_theme_override_properties

    out: AssetBundleExportJobThemeOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_theme_override_properties.deserialize_json(
                item
            )
        )
    return out
