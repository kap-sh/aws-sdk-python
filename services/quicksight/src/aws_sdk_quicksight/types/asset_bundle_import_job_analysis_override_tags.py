"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideTags``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list
    import aws_sdk_quicksight.types.tag_list


class AssetBundleImportJobAnalysisOverrideTags(TypedDict):
    analysis_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of analysis IDs that you want to apply overrides to. You can use <code>*</code> to override all analyses in this asset bundle.</p>"""
    tags: "aws_sdk_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the analyses that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideTags) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["AnalysisIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["analysis_ids"]
        )
    )
    import aws_sdk_quicksight.types.tag_list

    out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverrideTags:
    out: AssetBundleImportJobAnalysisOverrideTags = {}  # type: ignore[typeddict-item]
    if "AnalysisIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["analysis_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["AnalysisIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverrideTags.analysis_ids required"
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverrideTags.tags required"
        )
    return out
