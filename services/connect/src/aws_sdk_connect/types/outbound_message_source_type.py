"""Generated from Smithy shape ``com.amazonaws.connect#OutboundMessageSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

OutboundMessageSourceType: TypeAlias = Literal[
    "TEMPLATE",
    "RAW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEMPLATE",
        "RAW",
    )
)


def serialize_json(value: OutboundMessageSourceType) -> str:
    return value


def deserialize_json(data: str) -> OutboundMessageSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutboundMessageSourceType value: {data!r}")
    return cast(OutboundMessageSourceType, data)
