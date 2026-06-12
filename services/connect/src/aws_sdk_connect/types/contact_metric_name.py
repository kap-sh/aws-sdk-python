"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactMetricName: TypeAlias = Literal[
    "ESTIMATED_WAIT_TIME",
    "POSITION_IN_QUEUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ESTIMATED_WAIT_TIME",
        "POSITION_IN_QUEUE",
    )
)


def serialize_json(value: ContactMetricName) -> str:
    return value


def deserialize_json(data: str) -> ContactMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactMetricName value: {data!r}")
    return cast(ContactMetricName, data)
