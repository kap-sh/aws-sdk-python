"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_value_override

SlotValues: TypeAlias = list[
    "capo_lex_models_v2.types.slot_value_override.SlotValueOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotValues) -> list:
    import capo_lex_models_v2.types.slot_value_override

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_value_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotValues:
    import capo_lex_models_v2.types.slot_value_override

    out: SlotValues = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_value_override.deserialize_json(item))
    return out
