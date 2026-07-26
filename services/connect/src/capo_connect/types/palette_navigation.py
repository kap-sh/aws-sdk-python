"""Generated from Smithy shape ``com.amazonaws.connect#PaletteNavigation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.theme_string


class PaletteNavigation(TypedDict, closed=True):
    background: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The background color of the navigation area.</p>"""
    text_background_hover: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The background color when hovering over navigation text.</p>"""
    text_background_active: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The background color for active navigation items.</p>"""
    text: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The text color in the navigation area.</p>"""
    text_hover: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The text color when hovering over navigation items.</p>"""
    text_active: NotRequired["capo_connect.types.theme_string.ThemeString"]
    """<p>The text color for active navigation items.</p>"""
    invert_actions_colors: "capo_connect.types.boolean.Boolean"
    """<p>Whether to invert the colors of action buttons in the navigation area.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaletteNavigation) -> dict:
    out: dict = {}
    if "background" in value:
        out["Background"] = value["background"]
    if "text_background_hover" in value:
        out["TextBackgroundHover"] = value["text_background_hover"]
    if "text_background_active" in value:
        out["TextBackgroundActive"] = value["text_background_active"]
    if "text" in value:
        out["Text"] = value["text"]
    if "text_hover" in value:
        out["TextHover"] = value["text_hover"]
    if "text_active" in value:
        out["TextActive"] = value["text_active"]
    out["InvertActionsColors"] = value.get("invert_actions_colors", False)
    return out


def deserialize_json(data: dict) -> PaletteNavigation:
    out: PaletteNavigation = {}  # type: ignore[typeddict-item]
    if "Background" in data:
        out["background"] = data["Background"]
    if "TextBackgroundHover" in data:
        out["text_background_hover"] = data["TextBackgroundHover"]
    if "TextBackgroundActive" in data:
        out["text_background_active"] = data["TextBackgroundActive"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "TextHover" in data:
        out["text_hover"] = data["TextHover"]
    if "TextActive" in data:
        out["text_active"] = data["TextActive"]
    if "InvertActionsColors" in data:
        out["invert_actions_colors"] = data["InvertActionsColors"]
    else:
        out["invert_actions_colors"] = False
    return out
