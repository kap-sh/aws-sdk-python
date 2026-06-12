"""Generated from Smithy shape ``com.amazonaws.timestreamquery#S3EncryptionOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

S3EncryptionOption: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSE_S3",
        "SSE_KMS",
    )
)


def serialize_aws_json_1_0(value: S3EncryptionOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> S3EncryptionOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3EncryptionOption value: {data!r}")
    return cast(S3EncryptionOption, data)
