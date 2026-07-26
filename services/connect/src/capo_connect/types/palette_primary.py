"""Generated from Smithy shape ``com.amazonaws.connect#PalettePrimary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.theme_string


class PalettePrimary(TypedDict, closed=True):
    default: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The default primary color used throughout the workspace.</p>"""
    active: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The primary color used for active states.</p>"""
    contrast_text: NotRequired["capo_connect.types.theme_string.ThemeString"]
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
