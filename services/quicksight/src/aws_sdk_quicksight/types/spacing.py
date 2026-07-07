"""Generated from Smithy shape ``com.amazonaws.quicksight#Spacing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.length


class Spacing(TypedDict, closed=True):
    top: NotRequired["aws_sdk_quicksight.types.length.Length"]
    """<p>Define the top spacing.</p>"""
    bottom: NotRequired["aws_sdk_quicksight.types.length.Length"]
    """<p>Define the bottom spacing.</p>"""
    left: NotRequired["aws_sdk_quicksight.types.length.Length"]
    """<p>Define the left spacing.</p>"""
    right: NotRequired["aws_sdk_quicksight.types.length.Length"]
    """<p>Define the right spacing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Spacing) -> dict:
    out: dict = {}
    if "top" in value:
        out["Top"] = value["top"]
    if "bottom" in value:
        out["Bottom"] = value["bottom"]
    if "left" in value:
        out["Left"] = value["left"]
    if "right" in value:
        out["Right"] = value["right"]
    return out


def deserialize_json(data: dict) -> Spacing:
    out: Spacing = {}  # type: ignore[typeddict-item]
    if "Top" in data:
        out["top"] = data["Top"]
    if "Bottom" in data:
        out["bottom"] = data["Bottom"]
    if "Left" in data:
        out["left"] = data["Left"]
    if "Right" in data:
        out["right"] = data["Right"]
    return out
