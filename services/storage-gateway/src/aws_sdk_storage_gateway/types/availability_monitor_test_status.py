"""Generated from Smithy shape ``com.amazonaws.storagegateway#AvailabilityMonitorTestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

AvailabilityMonitorTestStatus: TypeAlias = Literal[
    "COMPLETE",
    "FAILED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "FAILED",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: AvailabilityMonitorTestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityMonitorTestStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AvailabilityMonitorTestStatus value: {data!r}"
        )
    return cast(AvailabilityMonitorTestStatus, data)
