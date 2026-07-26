"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestProtocol``."""

from typing import Literal, TypeAlias, cast

IngestProtocol: TypeAlias = Literal[
    "RTMP",
    "RTMPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestProtocol) -> str:
    return value


def deserialize_json(data: str) -> IngestProtocol:
    return cast(IngestProtocol, data)
