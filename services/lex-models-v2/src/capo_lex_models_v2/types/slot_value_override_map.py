"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueOverrideMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.slot_value_override

SlotValueOverrideMap: TypeAlias = dict[
    "capo_lex_models_v2.types.name.Name",
    "capo_lex_models_v2.types.slot_value_override.SlotValueOverride",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SlotValueOverrideMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.slot_value_override

        out[key] = capo_lex_models_v2.types.slot_value_override.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SlotValueOverrideMap:
    out: SlotValueOverrideMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.slot_value_override

        out[key] = capo_lex_models_v2.types.slot_value_override.deserialize_json(value)
    return out
