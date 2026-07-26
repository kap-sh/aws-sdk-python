"""Generated from Smithy shape ``com.amazonaws.storagegateway#AvailabilityMonitorTestStatus``."""

from typing import Literal, TypeAlias, cast

AvailabilityMonitorTestStatus: TypeAlias = Literal[
    "COMPLETE",
    "FAILED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityMonitorTestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityMonitorTestStatus:
    return cast(AvailabilityMonitorTestStatus, data)
