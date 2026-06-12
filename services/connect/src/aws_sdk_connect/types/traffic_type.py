"""Generated from Smithy shape ``com.amazonaws.connect#TrafficType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TrafficType: TypeAlias = Literal[
    "GENERAL",
    "CAMPAIGN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERAL",
        "CAMPAIGN",
    )
)


def serialize_json(value: TrafficType) -> str:
    return value


def deserialize_json(data: str) -> TrafficType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficType value: {data!r}")
    return cast(TrafficType, data)
