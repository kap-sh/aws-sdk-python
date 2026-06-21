"""Generated from Smithy shape ``com.amazonaws.backupsearch#LongConditionOperator``."""

from typing import Literal, TypeAlias, cast

LongConditionOperator: TypeAlias = Literal[
    "EQUALS_TO",
    "NOT_EQUALS_TO",
    "LESS_THAN_EQUAL_TO",
    "GREATER_THAN_EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: LongConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> LongConditionOperator:
    return cast(LongConditionOperator, data)
