"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleClusterMarker``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class SimpleClusterMarker(TypedDict):
    color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the simple cluster marker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleClusterMarker) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> SimpleClusterMarker:
    out: SimpleClusterMarker = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    return out
