"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.count


class SlotTypeStatistics(TypedDict):
    discovered_slot_type_count: NotRequired["aws_sdk_lex_models_v2.types.count.Count"]
    """<p>The number of recommended slot types associated with the bot recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeStatistics) -> dict:
    out: dict = {}
    if "discovered_slot_type_count" in value:
        out["discoveredSlotTypeCount"] = value["discovered_slot_type_count"]
    return out


def deserialize_json(data: dict) -> SlotTypeStatistics:
    out: SlotTypeStatistics = {}  # type: ignore[typeddict-item]
    if "discoveredSlotTypeCount" in data:
        out["discovered_slot_type_count"] = data["discoveredSlotTypeCount"]
    return out
