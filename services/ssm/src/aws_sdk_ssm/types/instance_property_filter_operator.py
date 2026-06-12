"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InstancePropertyFilterOperator: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
    "LessThan",
    "GreaterThan",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equal",
        "NotEqual",
        "BeginWith",
        "LessThan",
        "GreaterThan",
    )
)


def serialize_aws_json_1_1(value: InstancePropertyFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePropertyFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstancePropertyFilterOperator value: {data!r}"
        )
    return cast(InstancePropertyFilterOperator, data)
