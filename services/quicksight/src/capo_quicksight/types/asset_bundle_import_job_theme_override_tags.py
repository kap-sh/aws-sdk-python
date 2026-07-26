"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list
    import capo_quicksight.types.tag_list


class AssetBundleImportJobThemeOverrideTags(TypedDict, closed=True):
    theme_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of theme IDs that you want to apply overrides to. You can use <code>*</code> to override all themes in this asset bundle.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the themes that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverrideTags) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["ThemeIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["theme_ids"]
        )
    )
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobThemeOverrideTags:
    out: AssetBundleImportJobThemeOverrideTags = {}  # type: ignore[typeddict-item]
    if "ThemeIds" in data:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["theme_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["ThemeIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobThemeOverrideTags.theme_ids required"
        )
    if "Tags" in data:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobThemeOverrideTags.tags required"
        )
    return out
