"""Generated from Smithy shape ``com.amazonaws.ebs#SSEType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

SSEType: TypeAlias = Literal[
    "sse-ebs",
    "sse-kms",
    "none",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sse-ebs",
        "sse-kms",
        "none",
    )
)


def serialize_json(value: SSEType) -> str:
    return value


def deserialize_json(data: str) -> SSEType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEType value: {data!r}")
    return cast(SSEType, data)
