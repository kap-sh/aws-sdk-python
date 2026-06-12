"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConditionOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ConditionOperatorType: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThen",
    "GreaterOrEquals",
    "LessThen",
    "LessOrEquals",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "NotEquals",
        "GreaterThen",
        "GreaterOrEquals",
        "LessThen",
        "LessOrEquals",
    )
)


def serialize_json(value: ConditionOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ConditionOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionOperatorType value: {data!r}")
    return cast(ConditionOperatorType, data)
