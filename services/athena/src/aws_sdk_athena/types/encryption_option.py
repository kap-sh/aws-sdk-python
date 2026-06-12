"""Generated from Smithy shape ``com.amazonaws.athena#EncryptionOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

EncryptionOption: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
    "CSE_KMS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSE_S3",
        "SSE_KMS",
        "CSE_KMS",
    )
)


def serialize_aws_json_1_1(value: EncryptionOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionOption value: {data!r}")
    return cast(EncryptionOption, data)
