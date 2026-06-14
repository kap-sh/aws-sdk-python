"""Generated from Smithy shape ``com.amazonaws.storagegateway#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "SseS3",
    "SseKms",
    "DsseKms",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SseS3",
        "SseKms",
        "DsseKms",
    )
)


def serialize_aws_json_1_1(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
