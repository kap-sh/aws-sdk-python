"""Generated from Smithy shape ``com.amazonaws.backupsearch#TimeConditionOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backupsearch.errors import DeserializationError

TimeConditionOperator: TypeAlias = Literal[
    "EQUALS_TO",
    "NOT_EQUALS_TO",
    "LESS_THAN_EQUAL_TO",
    "GREATER_THAN_EQUAL_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS_TO",
        "NOT_EQUALS_TO",
        "LESS_THAN_EQUAL_TO",
        "GREATER_THAN_EQUAL_TO",
    )
)


def serialize_json(value: TimeConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> TimeConditionOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeConditionOperator value: {data!r}")
    return cast(TimeConditionOperator, data)
