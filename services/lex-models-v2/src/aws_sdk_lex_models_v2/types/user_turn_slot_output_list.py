"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnSlotOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.user_turn_slot_output

UserTurnSlotOutputList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.user_turn_slot_output.UserTurnSlotOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnSlotOutputList) -> list:
    import aws_sdk_lex_models_v2.types.user_turn_slot_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.user_turn_slot_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserTurnSlotOutputList:
    import aws_sdk_lex_models_v2.types.user_turn_slot_output

    out: UserTurnSlotOutputList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.user_turn_slot_output.deserialize_json(item)
        )
    return out
