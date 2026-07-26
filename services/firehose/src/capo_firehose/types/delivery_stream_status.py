"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamStatus``."""

from typing import Literal, TypeAlias, cast

DeliveryStreamStatus: TypeAlias = Literal[
    "CREATING",
    "CREATING_FAILED",
    "DELETING",
    "DELETING_FAILED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamStatus:
    return cast(DeliveryStreamStatus, data)
