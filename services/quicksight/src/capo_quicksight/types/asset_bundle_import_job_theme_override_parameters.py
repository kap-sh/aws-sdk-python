"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name


class AssetBundleImportJobThemeOverrideParameters(TypedDict, closed=True):
    theme_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the theme to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverrideParameters) -> dict:
    out: dict = {}
    out["ThemeId"] = value["theme_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobThemeOverrideParameters:
    out: AssetBundleImportJobThemeOverrideParameters = {}  # type: ignore[typeddict-item]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobThemeOverrideParameters.theme_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
