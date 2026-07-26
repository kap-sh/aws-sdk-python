"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: DeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStatus:
    return cast(DeliveryStatus, data)
