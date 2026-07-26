"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotPriority``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.priority_value


class SlotPriority(TypedDict, closed=True):
    priority: "capo_lex_models_v2.types.priority_value.PriorityValue"
    """<p>The priority that Amazon Lex should apply to the slot.</p>"""
    slot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotPriority) -> dict:
    out: dict = {}
    out["priority"] = value["priority"]
    out["slotId"] = value["slot_id"]
    return out


def deserialize_json(data: dict) -> SlotPriority:
    out: SlotPriority = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("SlotPriority.priority required")
    if "slotId" in data:
        out["slot_id"] = data["slotId"]
    else:
        raise DeserializationError("SlotPriority.slot_id required")
    return out
