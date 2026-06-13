"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters

AssetBundleImportJobThemeOverrideParametersList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters.AssetBundleImportJobThemeOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverrideParametersList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobThemeOverrideParametersList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters

    out: AssetBundleImportJobThemeOverrideParametersList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_theme_override_parameters.deserialize_json(
                item
            )
        )
    return out
