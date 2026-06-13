"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters

AssetBundleImportJobAnalysisOverrideParametersList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters.AssetBundleImportJobAnalysisOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideParametersList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobAnalysisOverrideParametersList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters

    out: AssetBundleImportJobAnalysisOverrideParametersList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_analysis_override_parameters.deserialize_json(
                item
            )
        )
    return out
