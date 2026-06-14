"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

FilterOperator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThan",
    "LessThan",
    "GreaterThanOrEqual",
    "LessThanOrEqual",
    "Contains",
    "NotContains",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "NotEquals",
        "GreaterThan",
        "LessThan",
        "GreaterThanOrEqual",
        "LessThanOrEqual",
        "Contains",
        "NotContains",
    )
)


def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperator value: {data!r}")
    return cast(FilterOperator, data)
