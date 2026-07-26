"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinIntentSlotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_intent_slot

BuiltinIntentSlotList: TypeAlias = list[
    "capo_lex_model_building_service.types.builtin_intent_slot.BuiltinIntentSlot"
]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinIntentSlotList) -> list:
    import capo_lex_model_building_service.types.builtin_intent_slot

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.builtin_intent_slot.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BuiltinIntentSlotList:
    import capo_lex_model_building_service.types.builtin_intent_slot

    out: BuiltinIntentSlotList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.builtin_intent_slot.deserialize_json(
                item
            )
        )
    return out
