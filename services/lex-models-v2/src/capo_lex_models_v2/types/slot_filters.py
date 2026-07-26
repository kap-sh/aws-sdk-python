"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_filter

SlotFilters: TypeAlias = list["capo_lex_models_v2.types.slot_filter.SlotFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: SlotFilters) -> list:
    import capo_lex_models_v2.types.slot_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotFilters:
    import capo_lex_models_v2.types.slot_filter

    out: SlotFilters = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_filter.deserialize_json(item))
    return out
