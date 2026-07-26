"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags

AssetBundleImportJobAnalysisOverrideTagsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_analysis_override_tags.AssetBundleImportJobAnalysisOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideTagsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_analysis_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobAnalysisOverrideTagsList:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_tags

    out: AssetBundleImportJobAnalysisOverrideTagsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_analysis_override_tags.deserialize_json(
                item
            )
        )
    return out
