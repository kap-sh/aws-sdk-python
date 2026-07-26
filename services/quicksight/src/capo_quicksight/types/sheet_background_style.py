"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetBackgroundStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.color
    import capo_quicksight.types.string


class SheetBackgroundStyle(TypedDict, closed=True):
    color: NotRequired["capo_quicksight.types.color.Color"]
    """<p>The solid color background option for sheets.</p>"""
    gradient: NotRequired["capo_quicksight.types.string.String"]
    """<p>The gradient background option for sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetBackgroundStyle) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    if "gradient" in value:
        out["Gradient"] = value["gradient"]
    return out


def deserialize_json(data: dict) -> SheetBackgroundStyle:
    out: SheetBackgroundStyle = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    if "Gradient" in data:
        out["gradient"] = data["Gradient"]
    return out
