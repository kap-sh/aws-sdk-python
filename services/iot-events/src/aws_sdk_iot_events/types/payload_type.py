"""Generated from Smithy shape ``com.amazonaws.iotevents#PayloadType``."""

from typing import Literal, TypeAlias, cast

PayloadType: TypeAlias = Literal[
    "STRING",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadType) -> str:
    return value


def deserialize_json(data: str) -> PayloadType:
    return cast(PayloadType, data)
