"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleClusterMarker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color


class SimpleClusterMarker(TypedDict, closed=True):
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
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
