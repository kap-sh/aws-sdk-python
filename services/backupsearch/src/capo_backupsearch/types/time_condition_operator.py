"""Generated from Smithy shape ``com.amazonaws.backupsearch#TimeConditionOperator``."""

from typing import Literal, TypeAlias, cast

TimeConditionOperator: TypeAlias = Literal[
    "EQUALS_TO",
    "NOT_EQUALS_TO",
    "LESS_THAN_EQUAL_TO",
    "GREATER_THAN_EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> TimeConditionOperator:
    return cast(TimeConditionOperator, data)
