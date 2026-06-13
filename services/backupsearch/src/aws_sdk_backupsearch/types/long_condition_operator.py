"""Generated from Smithy shape ``com.amazonaws.backupsearch#LongConditionOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backupsearch.errors import DeserializationError

LongConditionOperator: TypeAlias = Literal[
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


def serialize_json(value: LongConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> LongConditionOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LongConditionOperator value: {data!r}")
    return cast(LongConditionOperator, data)
