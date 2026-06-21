"""Generated from Smithy shape ``com.amazonaws.cognitosync#Operation``."""

from typing import Literal, TypeAlias, cast

Operation: TypeAlias = Literal[
    "replace",
    "remove",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operation) -> str:
    return value


def deserialize_json(data: str) -> Operation:
    return cast(Operation, data)
