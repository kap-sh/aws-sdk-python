"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_default_value

SlotDefaultValueList: TypeAlias = list[
    "capo_lex_models_v2.types.slot_default_value.SlotDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValueList) -> list:
    import capo_lex_models_v2.types.slot_default_value

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_default_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotDefaultValueList:
    import capo_lex_models_v2.types.slot_default_value

    out: SlotDefaultValueList = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_default_value.deserialize_json(item))
    return out
