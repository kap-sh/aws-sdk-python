"""Generated from Smithy shape ``com.amazonaws.kinesis#ConsumerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.consumer

ConsumerList: TypeAlias = list["aws_sdk_kinesis.types.consumer.Consumer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumerList) -> list:
    import aws_sdk_kinesis.types.consumer

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis.types.consumer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConsumerList:
    import aws_sdk_kinesis.types.consumer

    out: ConsumerList = []
    for item in data:
        out.append(aws_sdk_kinesis.types.consumer.deserialize_aws_json_1_1(item))
    return out
