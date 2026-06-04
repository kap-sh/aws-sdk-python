"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnValue``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ReturnValue: TypeAlias = Literal[
    "NONE",
    "ALL_OLD",
    "UPDATED_OLD",
    "ALL_NEW",
    "UPDATED_NEW",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ALL_OLD",
        "UPDATED_OLD",
        "ALL_NEW",
        "UPDATED_NEW",
    )
)


def serialize_aws_json_1_0(value: ReturnValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReturnValue value: {data!r}")
    return cast(ReturnValue, data)
