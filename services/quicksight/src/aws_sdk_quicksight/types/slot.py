"""Generated from Smithy shape ``com.amazonaws.quicksight#Slot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string


class Slot(TypedDict, closed=True):
    slot_id: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The slot ID of the slot.</p>"""
    visual_id: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The visual ID for the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Slot) -> dict:
    out: dict = {}
    if "slot_id" in value:
        out["SlotId"] = value["slot_id"]
    if "visual_id" in value:
        out["VisualId"] = value["visual_id"]
    return out


def deserialize_json(data: dict) -> Slot:
    out: Slot = {}  # type: ignore[typeddict-item]
    if "SlotId" in data:
        out["slot_id"] = data["SlotId"]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    return out
