"""Generated from Smithy shape ``com.amazonaws.backupsearch#StringConditionOperator``."""

from typing import Literal, TypeAlias, cast

StringConditionOperator: TypeAlias = Literal[
    "EQUALS_TO",
    "NOT_EQUALS_TO",
    "CONTAINS",
    "DOES_NOT_CONTAIN",
    "BEGINS_WITH",
    "ENDS_WITH",
    "DOES_NOT_BEGIN_WITH",
    "DOES_NOT_END_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: StringConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> StringConditionOperator:
    return cast(StringConditionOperator, data)
