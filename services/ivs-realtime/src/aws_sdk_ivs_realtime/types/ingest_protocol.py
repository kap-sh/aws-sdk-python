"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

IngestProtocol: TypeAlias = Literal[
    "RTMP",
    "RTMPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RTMP",
        "RTMPS",
    )
)


def serialize_json(value: IngestProtocol) -> str:
    return value


def deserialize_json(data: str) -> IngestProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestProtocol value: {data!r}")
    return cast(IngestProtocol, data)
