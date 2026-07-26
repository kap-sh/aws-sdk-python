"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinationType``."""

from typing import Literal, TypeAlias, cast

DeliveryDestinationType: TypeAlias = Literal[
    "S3",
    "CWL",
    "FH",
    "XRAY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryDestinationType:
    return cast(DeliveryDestinationType, data)
