"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobAnalysisOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_analysis_override_properties

AssetBundleExportJobAnalysisOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_analysis_override_properties.AssetBundleExportJobAnalysisOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobAnalysisOverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_analysis_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_analysis_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobAnalysisOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_analysis_override_properties

    out: AssetBundleExportJobAnalysisOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_analysis_override_properties.deserialize_json(
                item
            )
        )
    return out
