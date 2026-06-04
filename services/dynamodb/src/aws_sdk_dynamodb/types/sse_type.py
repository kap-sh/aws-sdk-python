"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

SSEType: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "KMS",
    )
)


def serialize_aws_json_1_0(value: SSEType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SSEType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEType value: {data!r}")
    return cast(SSEType, data)
