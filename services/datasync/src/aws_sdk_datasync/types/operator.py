"""Generated from Smithy shape ``com.amazonaws.datasync#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

Operator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "In",
    "LessThanOrEqual",
    "LessThan",
    "GreaterThanOrEqual",
    "GreaterThan",
    "Contains",
    "NotContains",
    "BeginsWith",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "NotEquals",
        "In",
        "LessThanOrEqual",
        "LessThan",
        "GreaterThanOrEqual",
        "GreaterThan",
        "Contains",
        "NotContains",
        "BeginsWith",
    )
)


def serialize_aws_json_1_1(value: Operator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
