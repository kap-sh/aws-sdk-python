"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyProviderInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

EncryptionKeyProviderInput: TypeAlias = Literal[
    "ORACLE_MANAGED",
    "AWS_KMS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORACLE_MANAGED",
        "AWS_KMS",
    )
)


def serialize_aws_json_1_0(value: EncryptionKeyProviderInput) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionKeyProviderInput:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EncryptionKeyProviderInput value: {data!r}"
        )
    return cast(EncryptionKeyProviderInput, data)
