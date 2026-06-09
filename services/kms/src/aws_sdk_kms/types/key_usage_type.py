"""Generated from Smithy shape ``com.amazonaws.kms#KeyUsageType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

KeyUsageType: TypeAlias = Literal[
    "SIGN_VERIFY",
    "ENCRYPT_DECRYPT",
    "GENERATE_VERIFY_MAC",
    "KEY_AGREEMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIGN_VERIFY",
        "ENCRYPT_DECRYPT",
        "GENERATE_VERIFY_MAC",
        "KEY_AGREEMENT",
    )
)


def serialize_aws_json_1_1(value: KeyUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyUsageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyUsageType value: {data!r}")
    return cast(KeyUsageType, data)
