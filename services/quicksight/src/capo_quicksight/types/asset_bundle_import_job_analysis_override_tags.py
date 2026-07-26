"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list
    import capo_quicksight.types.tag_list


class AssetBundleImportJobAnalysisOverrideTags(TypedDict, closed=True):
    analysis_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of analysis IDs that you want to apply overrides to. You can use <code>*</code> to override all analyses in this asset bundle.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the analyses that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideTags) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["AnalysisIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["analysis_ids"]
        )
    )
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverrideTags:
    out: AssetBundleImportJobAnalysisOverrideTags = {}  # type: ignore[typeddict-item]
    if "AnalysisIds" in data:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["analysis_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["AnalysisIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverrideTags.analysis_ids required"
        )
    if "Tags" in data:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverrideTags.tags required"
        )
    return out
