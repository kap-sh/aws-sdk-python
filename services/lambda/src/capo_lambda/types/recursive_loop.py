"""Generated from Smithy shape ``com.amazonaws.lambda#RecursiveLoop``."""

from typing import Literal, TypeAlias, cast

RecursiveLoop: TypeAlias = Literal[
    "Allow",
    "Terminate",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecursiveLoop) -> str:
    return value


def deserialize_json(data: str) -> RecursiveLoop:
    return cast(RecursiveLoop, data)
