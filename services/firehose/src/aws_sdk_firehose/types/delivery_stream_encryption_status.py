"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamEncryptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DeliveryStreamEncryptionStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "ENABLING_FAILED",
    "DISABLED",
    "DISABLING",
    "DISABLING_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "ENABLING",
        "ENABLING_FAILED",
        "DISABLED",
        "DISABLING",
        "DISABLING_FAILED",
    )
)


def serialize_aws_json_1_1(value: DeliveryStreamEncryptionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamEncryptionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeliveryStreamEncryptionStatus value: {data!r}"
        )
    return cast(DeliveryStreamEncryptionStatus, data)
