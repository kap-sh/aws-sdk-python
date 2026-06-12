"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "KMS_BASED_ENCRYPTION",
    "FLEETWISE_DEFAULT_ENCRYPTION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KMS_BASED_ENCRYPTION",
        "FLEETWISE_DEFAULT_ENCRYPTION",
    )
)


def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
