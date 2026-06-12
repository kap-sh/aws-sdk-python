"""Generated from Smithy shape ``com.amazonaws.kafka#CustomerActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>A type of an action required from the customer.</p>"""
CustomerActionStatus: TypeAlias = Literal[
    "CRITICAL_ACTION_REQUIRED",
    "ACTION_RECOMMENDED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL_ACTION_REQUIRED",
        "ACTION_RECOMMENDED",
        "NONE",
    )
)


def serialize_json(value: CustomerActionStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomerActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerActionStatus value: {data!r}")
    return cast(CustomerActionStatus, data)
