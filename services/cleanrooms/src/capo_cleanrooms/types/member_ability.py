"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberAbility``."""

from typing import Literal, TypeAlias, cast

MemberAbility: TypeAlias = Literal[
    "CAN_QUERY",
    "CAN_RECEIVE_RESULTS",
    "CAN_RUN_JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAbility) -> str:
    return value


def deserialize_json(data: str) -> MemberAbility:
    return cast(MemberAbility, data)
