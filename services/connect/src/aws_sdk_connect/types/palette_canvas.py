"""Generated from Smithy shape ``com.amazonaws.connect#PaletteCanvas``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.theme_string


class PaletteCanvas(TypedDict):
    container_background: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The background color for container elements.</p>"""
    page_background: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The background color for page elements.</p>"""
    active_background: NotRequired["aws_sdk_connect.types.theme_string.ThemeString"]
    """<p>The background color for active elements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaletteCanvas) -> dict:
    out: dict = {}
    if "container_background" in value:
        out["ContainerBackground"] = value["container_background"]
    if "page_background" in value:
        out["PageBackground"] = value["page_background"]
    if "active_background" in value:
        out["ActiveBackground"] = value["active_background"]
    return out


def deserialize_json(data: dict) -> PaletteCanvas:
    out: PaletteCanvas = {}  # type: ignore[typeddict-item]
    if "ContainerBackground" in data:
        out["container_background"] = data["ContainerBackground"]
    if "PageBackground" in data:
        out["page_background"] = data["PageBackground"]
    if "ActiveBackground" in data:
        out["active_background"] = data["ActiveBackground"]
    return out
