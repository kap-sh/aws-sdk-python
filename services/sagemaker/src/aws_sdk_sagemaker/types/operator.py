"""Generated from Smithy shape ``com.amazonaws.sagemaker#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Operator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "LessThan",
    "LessThanOrEqualTo",
    "Contains",
    "Exists",
    "NotExists",
    "In",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "NotEquals",
        "GreaterThan",
        "GreaterThanOrEqualTo",
        "LessThan",
        "LessThanOrEqualTo",
        "Contains",
        "Exists",
        "NotExists",
        "In",
    )
)


def serialize_aws_json_1_1(value: Operator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
