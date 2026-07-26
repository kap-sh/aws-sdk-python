"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Quality``."""

from typing import Literal, TypeAlias, cast

Quality: TypeAlias = Literal[
    "GOOD",
    "BAD",
    "UNCERTAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: Quality) -> str:
    return value


def deserialize_json(data: str) -> Quality:
    return cast(Quality, data)
