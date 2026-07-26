"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnSlotOutputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.user_turn_slot_output

UserTurnSlotOutputMap: TypeAlias = dict[
    "capo_lex_models_v2.types.name.Name",
    "capo_lex_models_v2.types.user_turn_slot_output.UserTurnSlotOutput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UserTurnSlotOutputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.user_turn_slot_output

        out[key] = capo_lex_models_v2.types.user_turn_slot_output.serialize_json(value)
    return out


def deserialize_json(data: dict) -> UserTurnSlotOutputMap:
    out: UserTurnSlotOutputMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.user_turn_slot_output

        out[key] = capo_lex_models_v2.types.user_turn_slot_output.deserialize_json(
            value
        )
    return out
