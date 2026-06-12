"""Generated from Smithy shape ``com.amazonaws.transfer#EncryptionAlg``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

EncryptionAlg: TypeAlias = Literal[
    "AES128_CBC",
    "AES192_CBC",
    "AES256_CBC",
    "DES_EDE3_CBC",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES128_CBC",
        "AES192_CBC",
        "AES256_CBC",
        "DES_EDE3_CBC",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: EncryptionAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionAlg:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionAlg value: {data!r}")
    return cast(EncryptionAlg, data)
