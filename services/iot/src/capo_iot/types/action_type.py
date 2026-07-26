"""Generated from Smithy shape ``com.amazonaws.iot#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "PUBLISH",
    "SUBSCRIBE",
    "RECEIVE",
    "CONNECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    return cast(ActionType, data)
