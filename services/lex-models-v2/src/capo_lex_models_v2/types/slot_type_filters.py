"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_type_filter

SlotTypeFilters: TypeAlias = list[
    "capo_lex_models_v2.types.slot_type_filter.SlotTypeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeFilters) -> list:
    import capo_lex_models_v2.types.slot_type_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_type_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotTypeFilters:
    import capo_lex_models_v2.types.slot_type_filter

    out: SlotTypeFilters = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_type_filter.deserialize_json(item))
    return out
