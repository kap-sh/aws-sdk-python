"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "JPEG",
    "PNG",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
