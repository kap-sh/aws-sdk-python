"""Generated from Smithy shape ``com.amazonaws.connect#PalettePrimary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.theme_string


class PalettePrimary(TypedDict):
    default: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The default primary color used throughout the workspace.</p>"""
    active: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The primary color used for active states.</p>"""
    contrast_text: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The text color that contrasts with the primary color for readability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PalettePrimary) -> dict:
    out: dict = {}
    if "default" in value:
        out["Default"] = value["default"]
    if "active" in value:
        out["Active"] = value["active"]
    if "contrast_text" in value:
        out["ContrastText"] = value["contrast_text"]
    return out


def deserialize_json(data: dict) -> PalettePrimary:
    out: PalettePrimary = {}  # type: ignore[typeddict-item]
    if "Default" in data:
        out["default"] = data["Default"]
    if "Active" in data:
        out["active"] = data["Active"]
    if "ContrastText" in data:
        out["contrast_text"] = data["ContrastText"]
    return out
