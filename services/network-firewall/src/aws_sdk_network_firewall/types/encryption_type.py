"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "CUSTOMER_KMS",
    "AWS_OWNED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_KMS",
        "AWS_OWNED_KMS_KEY",
    )
)


def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
