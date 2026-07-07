"""Generated from Smithy shape ``com.amazonaws.connect#ImagesLogo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.theme_image_link


class ImagesLogo(TypedDict, closed=True):
    default: NotRequired["aws_sdk_connect.types.theme_image_link.ThemeImageLink"]
    """<p>The default logo image displayed in the workspace.</p>"""
    favicon: NotRequired["aws_sdk_connect.types.theme_image_link.ThemeImageLink"]
    """<p>The favicon image displayed in the browser tab.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImagesLogo) -> dict:
    out: dict = {}
    if "default" in value:
        out["Default"] = value["default"]
    if "favicon" in value:
        out["Favicon"] = value["favicon"]
    return out


def deserialize_json(data: dict) -> ImagesLogo:
    out: ImagesLogo = {}  # type: ignore[typeddict-item]
    if "Default" in data:
        out["default"] = data["Default"]
    if "Favicon" in data:
        out["favicon"] = data["Favicon"]
    return out
