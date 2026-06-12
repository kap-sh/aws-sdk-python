"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DeliveryStreamStatus: TypeAlias = Literal[
    "CREATING",
    "CREATING_FAILED",
    "DELETING",
    "DELETING_FAILED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATING_FAILED",
        "DELETING",
        "DELETING_FAILED",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: DeliveryStreamStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStreamStatus value: {data!r}")
    return cast(DeliveryStreamStatus, data)
