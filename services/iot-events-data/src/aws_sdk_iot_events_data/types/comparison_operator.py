"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "GREATER",
    "GREATER_OR_EQUAL",
    "LESS",
    "LESS_OR_EQUAL",
    "EQUAL",
    "NOT_EQUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER",
        "GREATER_OR_EQUAL",
        "LESS",
        "LESS_OR_EQUAL",
        "EQUAL",
        "NOT_EQUAL",
    )
)


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
