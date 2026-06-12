"""Generated from Smithy shape ``com.amazonaws.ecr#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "AES256",
    "KMS",
    "KMS_DSSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "KMS",
        "KMS_DSSE",
    )
)


def serialize_aws_json_1_1(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
