"""Generated from Smithy shape ``com.amazonaws.kms#GrantOperation``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

GrantOperation: TypeAlias = Literal[
    "Decrypt",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyWithoutPlaintext",
    "ReEncryptFrom",
    "ReEncryptTo",
    "Sign",
    "Verify",
    "GetPublicKey",
    "CreateGrant",
    "RetireGrant",
    "DescribeKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateMac",
    "VerifyMac",
    "DeriveSharedSecret",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Decrypt",
        "Encrypt",
        "GenerateDataKey",
        "GenerateDataKeyWithoutPlaintext",
        "ReEncryptFrom",
        "ReEncryptTo",
        "Sign",
        "Verify",
        "GetPublicKey",
        "CreateGrant",
        "RetireGrant",
        "DescribeKey",
        "GenerateDataKeyPair",
        "GenerateDataKeyPairWithoutPlaintext",
        "GenerateMac",
        "VerifyMac",
        "DeriveSharedSecret",
    )
)


def serialize_aws_json_1_1(value: GrantOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GrantOperation value: {data!r}")
    return cast(GrantOperation, data)
