"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CustomMLMemberAbility``."""

from typing import Literal, TypeAlias, cast

CustomMLMemberAbility: TypeAlias = Literal[
    "CAN_RECEIVE_MODEL_OUTPUT",
    "CAN_RECEIVE_INFERENCE_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMLMemberAbility) -> str:
    return value


def deserialize_json(data: str) -> CustomMLMemberAbility:
    return cast(CustomMLMemberAbility, data)
