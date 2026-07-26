"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConditionOperatorType``."""

from typing import Literal, TypeAlias, cast

ConditionOperatorType: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThen",
    "GreaterOrEquals",
    "LessThen",
    "LessOrEquals",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ConditionOperatorType:
    return cast(ConditionOperatorType, data)
