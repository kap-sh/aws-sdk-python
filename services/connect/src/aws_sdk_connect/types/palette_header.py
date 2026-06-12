"""Generated from Smithy shape ``com.amazonaws.connect#PaletteHeader``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.theme_string


class PaletteHeader(TypedDict):
    background: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The background color of the header.</p>"""
    text: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The text color in the header.</p>"""
    text_hover: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The text color when hovering over header elements.</p>"""
    invert_actions_colors: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether to invert the colors of action buttons in the header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaletteHeader) -> dict:
    out: dict = {}
    if "background" in value:
        out["Background"] = value["background"]
    if "text" in value:
        out["Text"] = value["text"]
    if "text_hover" in value:
        out["TextHover"] = value["text_hover"]
    out["InvertActionsColors"] = value.get("invert_actions_colors", False)
    return out


def deserialize_json(data: dict) -> PaletteHeader:
    out: PaletteHeader = {}  # type: ignore[typeddict-item]
    if "Background" in data:
        out["background"] = data["Background"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "TextHover" in data:
        out["text_hover"] = data["TextHover"]
    if "InvertActionsColors" in data:
        out["invert_actions_colors"] = data["InvertActionsColors"]
    else:
        out["invert_actions_colors"] = False
    return out
