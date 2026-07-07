"""Generated from Smithy shape ``com.amazonaws.iot#KinesisAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.partition_key
    import aws_sdk_iot.types.stream_name


class KinesisAction(TypedDict, closed=True):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access to the Amazon Kinesis stream.</p>"""
    stream_name: "aws_sdk_iot.types.stream_name.StreamName"
    """<p>The name of the Amazon Kinesis stream.</p>"""
    partition_key: NotRequired["aws_sdk_iot.types.partition_key.PartitionKey"]
    """<p>The partition key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["streamName"] = value["stream_name"]
    if "partition_key" in value:
        out["partitionKey"] = value["partition_key"]
    return out


def deserialize_json(data: dict) -> KinesisAction:
    out: KinesisAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("KinesisAction.role_arn required")
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    else:
        raise DeserializationError("KinesisAction.stream_name required")
    if "partitionKey" in data:
        out["partition_key"] = data["partitionKey"]
    return out
