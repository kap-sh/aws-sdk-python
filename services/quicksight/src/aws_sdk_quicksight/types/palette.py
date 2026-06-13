"""Generated from Smithy shape ``com.amazonaws.quicksight#Palette``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class Palette(TypedDict):
    foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color.</p>"""
    background: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The background color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Palette) -> dict:
    out: dict = {}
    if "foreground" in value:
        out["Foreground"] = value["foreground"]
    if "background" in value:
        out["Background"] = value["background"]
    return out


def deserialize_json(data: dict) -> Palette:
    out: Palette = {}  # type: ignore[typeddict-item]
    if "Foreground" in data:
        out["foreground"] = data["Foreground"]
    if "Background" in data:
        out["background"] = data["Background"]
    return out
