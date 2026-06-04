"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputCompressionType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

InputCompressionType: TypeAlias = Literal[
    "GZIP",
    "ZSTD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "ZSTD",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: InputCompressionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InputCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputCompressionType value: {data!r}")
    return cast(InputCompressionType, data)
