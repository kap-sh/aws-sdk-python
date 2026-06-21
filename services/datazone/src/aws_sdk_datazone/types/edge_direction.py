"""Generated from Smithy shape ``com.amazonaws.datazone#EdgeDirection``."""

from typing import Literal, TypeAlias, cast

EdgeDirection: TypeAlias = Literal[
    "UPSTREAM",
    "DOWNSTREAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeDirection) -> str:
    return value


def deserialize_json(data: str) -> EdgeDirection:
    return cast(EdgeDirection, data)
