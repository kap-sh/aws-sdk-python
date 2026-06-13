"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobAnalysisPropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override

AssetBundleExportJobAnalysisPropertyToOverrideList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override.AssetBundleExportJobAnalysisPropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobAnalysisPropertyToOverrideList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobAnalysisPropertyToOverrideList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override

    out: AssetBundleExportJobAnalysisPropertyToOverrideList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_analysis_property_to_override.deserialize_json(
                item
            )
        )
    return out
