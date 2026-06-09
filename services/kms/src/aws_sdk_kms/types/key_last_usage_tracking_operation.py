"""Generated from Smithy shape ``com.amazonaws.kms#KeyLastUsageTrackingOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

KeyLastUsageTrackingOperation: TypeAlias = Literal[
    "Decrypt",
    "DeriveSharedSecret",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GenerateMac",
    "ReEncrypt",
    "Sign",
    "Verify",
    "VerifyMac",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Decrypt",
        "DeriveSharedSecret",
        "Encrypt",
        "GenerateDataKey",
        "GenerateDataKeyPair",
        "GenerateDataKeyPairWithoutPlaintext",
        "GenerateDataKeyWithoutPlaintext",
        "GenerateMac",
        "ReEncrypt",
        "Sign",
        "Verify",
        "VerifyMac",
    )
)


def serialize_aws_json_1_1(value: KeyLastUsageTrackingOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyLastUsageTrackingOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KeyLastUsageTrackingOperation value: {data!r}"
        )
    return cast(KeyLastUsageTrackingOperation, data)
