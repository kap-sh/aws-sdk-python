"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#State``."""

from typing import Literal, TypeAlias, cast

"""State"""
State: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: State) -> str:
    return value


def deserialize_json(data: str) -> State:
    return cast(State, data)
