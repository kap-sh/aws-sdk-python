"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SlotHintsIntentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.name
    import capo_lex_runtime_v2.types.slot_hints_slot_map

SlotHintsIntentMap: TypeAlias = dict[
    "capo_lex_runtime_v2.types.name.Name",
    "capo_lex_runtime_v2.types.slot_hints_slot_map.SlotHintsSlotMap",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SlotHintsIntentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_runtime_v2.types.slot_hints_slot_map

        out[key] = capo_lex_runtime_v2.types.slot_hints_slot_map.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SlotHintsIntentMap:
    out: SlotHintsIntentMap = {}
    for key, value in data.items():
        import capo_lex_runtime_v2.types.slot_hints_slot_map

        out[key] = capo_lex_runtime_v2.types.slot_hints_slot_map.deserialize_json(value)
    return out
