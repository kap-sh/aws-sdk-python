"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

DeliveryStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "FAILED_SIGNING_FILE",
    "PENDING",
    "RESOURCE_NOT_FOUND",
    "ACCESS_DENIED",
    "ACCESS_DENIED_SIGNING_FILE",
    "CANCELLED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
        "FAILED_SIGNING_FILE",
        "PENDING",
        "RESOURCE_NOT_FOUND",
        "ACCESS_DENIED",
        "ACCESS_DENIED_SIGNING_FILE",
        "CANCELLED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: DeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStatus value: {data!r}")
    return cast(DeliveryStatus, data)
