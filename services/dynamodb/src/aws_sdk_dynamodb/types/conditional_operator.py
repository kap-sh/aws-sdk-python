"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionalOperator``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ConditionalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_aws_json_1_0(value: ConditionalOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConditionalOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionalOperator value: {data!r}")
    return cast(ConditionalOperator, data)
