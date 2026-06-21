"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AllowMessages``."""

from typing import Literal, TypeAlias, cast

AllowMessages: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowMessages) -> str:
    return value


def deserialize_json(data: str) -> AllowMessages:
    return cast(AllowMessages, data)
