"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list
    import capo_quicksight.types.tag_list


class AssetBundleImportJobDataSetOverrideTags(TypedDict, closed=True):
    data_set_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of dataset IDs that you want to apply overrides to. You can use <code>*</code> to override all datasets in this asset bundle.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the datasets that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideTags) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DataSetIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["data_set_ids"]
        )
    )
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSetOverrideTags:
    out: AssetBundleImportJobDataSetOverrideTags = {}  # type: ignore[typeddict-item]
    if "DataSetIds" in data:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["data_set_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DataSetIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSetOverrideTags.data_set_ids required"
        )
    if "Tags" in data:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSetOverrideTags.tags required"
        )
    return out
