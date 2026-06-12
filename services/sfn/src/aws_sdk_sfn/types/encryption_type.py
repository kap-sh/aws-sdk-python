"""Generated from Smithy shape ``com.amazonaws.sfn#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KEY",
        "CUSTOMER_MANAGED_KMS_KEY",
    )
)


def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
