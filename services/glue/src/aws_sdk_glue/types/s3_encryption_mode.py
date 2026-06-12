"""Generated from Smithy shape ``com.amazonaws.glue#S3EncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

S3EncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
    "SSE-S3",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "SSE-KMS",
        "SSE-S3",
    )
)


def serialize_aws_json_1_1(value: S3EncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3EncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3EncryptionMode value: {data!r}")
    return cast(S3EncryptionMode, data)
