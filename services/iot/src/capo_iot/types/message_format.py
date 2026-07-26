"""Generated from Smithy shape ``com.amazonaws.iot#MessageFormat``."""

from typing import Literal, TypeAlias, cast

MessageFormat: TypeAlias = Literal[
    "RAW",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageFormat) -> str:
    return value


def deserialize_json(data: str) -> MessageFormat:
    return cast(MessageFormat, data)
