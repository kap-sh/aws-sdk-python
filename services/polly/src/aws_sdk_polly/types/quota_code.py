"""Generated from Smithy shape ``com.amazonaws.polly#QuotaCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

QuotaCode: TypeAlias = Literal[
    "input-stream-inbound-event-timeout",
    "input-stream-timeout",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "input-stream-inbound-event-timeout",
        "input-stream-timeout",
    )
)


def serialize_json(value: QuotaCode) -> str:
    return value


def deserialize_json(data: str) -> QuotaCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotaCode value: {data!r}")
    return cast(QuotaCode, data)
