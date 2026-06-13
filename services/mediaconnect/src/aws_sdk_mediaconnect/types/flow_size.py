"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FlowSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

FlowSize: TypeAlias = Literal[
    "MEDIUM",
    "LARGE",
    "LARGE_4X",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEDIUM",
        "LARGE",
        "LARGE_4X",
    )
)


def serialize_json(value: FlowSize) -> str:
    return value


def deserialize_json(data: str) -> FlowSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowSize value: {data!r}")
    return cast(FlowSize, data)
