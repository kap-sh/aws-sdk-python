"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBSecurityStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

SMBSecurityStrategy: TypeAlias = Literal[
    "ClientSpecified",
    "MandatorySigning",
    "MandatoryEncryption",
    "MandatoryEncryptionNoAes128",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClientSpecified",
        "MandatorySigning",
        "MandatoryEncryption",
        "MandatoryEncryptionNoAes128",
    )
)


def serialize_aws_json_1_1(value: SMBSecurityStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SMBSecurityStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SMBSecurityStrategy value: {data!r}")
    return cast(SMBSecurityStrategy, data)
