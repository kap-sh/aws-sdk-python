"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceStatus``."""

from typing import Literal, TypeAlias, cast

DeliverySourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceStatus:
    return cast(DeliverySourceStatus, data)
