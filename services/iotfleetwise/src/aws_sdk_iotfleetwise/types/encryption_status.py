"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

EncryptionStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "FAILURE",
    )
)


def serialize_aws_json_1_0(value: EncryptionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionStatus value: {data!r}")
    return cast(EncryptionStatus, data)
