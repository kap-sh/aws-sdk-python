"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotPrioritiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_priority

SlotPrioritiesList: TypeAlias = list[
    "capo_lex_models_v2.types.slot_priority.SlotPriority"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotPrioritiesList) -> list:
    import capo_lex_models_v2.types.slot_priority

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_priority.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotPrioritiesList:
    import capo_lex_models_v2.types.slot_priority

    out: SlotPrioritiesList = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_priority.deserialize_json(item))
    return out
