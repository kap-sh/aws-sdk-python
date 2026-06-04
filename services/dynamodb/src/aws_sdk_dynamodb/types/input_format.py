"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

InputFormat: TypeAlias = Literal[
    "DYNAMODB_JSON",
    "ION",
    "CSV",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DYNAMODB_JSON",
        "ION",
        "CSV",
    )
)


def serialize_aws_json_1_0(value: InputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputFormat value: {data!r}")
    return cast(InputFormat, data)
