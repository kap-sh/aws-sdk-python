"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.version_number


class ThemeAlias(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme alias.</p>"""
    alias_name: NotRequired["capo_quicksight.types.alias_name.AliasName"]
    """<p>The display name of the theme alias.</p>"""
    theme_version_number: NotRequired[
        "capo_quicksight.types.version_number.VersionNumber"
    ]
    """<p>The version number of the theme alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeAlias) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "theme_version_number" in value:
        out["ThemeVersionNumber"] = value["theme_version_number"]
    return out


def deserialize_json(data: dict) -> ThemeAlias:
    out: ThemeAlias = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "ThemeVersionNumber" in data:
        out["theme_version_number"] = data["ThemeVersionNumber"]
    return out
