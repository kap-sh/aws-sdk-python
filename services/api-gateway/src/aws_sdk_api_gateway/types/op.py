"""Generated from Smithy shape ``com.amazonaws.apigateway#Op``."""

from typing import Literal, TypeAlias, cast

Op: TypeAlias = Literal[
    "add",
    "remove",
    "replace",
    "move",
    "copy",
    "test",
]


# --- restJson1 ser/de ---
def serialize_json(value: Op) -> str:
    return value


def deserialize_json(data: str) -> Op:
    return cast(Op, data)
