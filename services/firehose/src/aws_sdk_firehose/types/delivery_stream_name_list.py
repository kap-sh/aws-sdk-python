"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name

DeliveryStreamNameList: TypeAlias = list[
    "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeliveryStreamNameList:
    return list(data)
