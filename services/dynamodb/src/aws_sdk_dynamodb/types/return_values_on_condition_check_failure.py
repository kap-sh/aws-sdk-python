"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnValuesOnConditionCheckFailure``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ReturnValuesOnConditionCheckFailure: TypeAlias = Literal[
    "ALL_OLD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_OLD",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: ReturnValuesOnConditionCheckFailure) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnValuesOnConditionCheckFailure:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReturnValuesOnConditionCheckFailure value: {data!r}"
        )
    return cast(ReturnValuesOnConditionCheckFailure, data)
