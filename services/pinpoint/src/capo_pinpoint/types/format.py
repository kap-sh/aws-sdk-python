"""Generated from Smithy shape ``com.amazonaws.pinpoint#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
