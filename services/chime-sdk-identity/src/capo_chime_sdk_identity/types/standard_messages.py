"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#StandardMessages``."""

from typing import Literal, TypeAlias, cast

StandardMessages: TypeAlias = Literal[
    "AUTO",
    "ALL",
    "MENTIONS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardMessages) -> str:
    return value


def deserialize_json(data: str) -> StandardMessages:
    return cast(StandardMessages, data)
