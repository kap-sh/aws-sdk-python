"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Include``."""

from typing import Literal, TypeAlias, cast

Include: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Include) -> str:
    return value


def deserialize_json(data: str) -> Include:
    return cast(Include, data)
