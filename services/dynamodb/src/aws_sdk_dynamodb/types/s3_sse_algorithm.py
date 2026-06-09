"""Generated from Smithy shape ``com.amazonaws.dynamodb#S3SseAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

S3SseAlgorithm: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: S3SseAlgorithm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> S3SseAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3SseAlgorithm value: {data!r}")
    return cast(S3SseAlgorithm, data)
