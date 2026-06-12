"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CommandParameterValueComparisonOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "LESS_THAN",
    "LESS_THAN_EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_EQUALS",
    "IN_SET",
    "NOT_IN_SET",
    "IN_RANGE",
    "NOT_IN_RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "LESS_THAN",
        "LESS_THAN_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_EQUALS",
        "IN_SET",
        "NOT_IN_SET",
        "IN_RANGE",
        "NOT_IN_RANGE",
    )
)


def serialize_json(value: CommandParameterValueComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> CommandParameterValueComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CommandParameterValueComparisonOperator value: {data!r}"
        )
    return cast(CommandParameterValueComparisonOperator, data)
