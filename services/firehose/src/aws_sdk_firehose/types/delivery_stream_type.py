"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamType``."""

from typing import Literal, TypeAlias, cast

DeliveryStreamType: TypeAlias = Literal[
    "DirectPut",
    "KinesisStreamAsSource",
    "MSKAsSource",
    "DatabaseAsSource",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamType:
    return cast(DeliveryStreamType, data)
