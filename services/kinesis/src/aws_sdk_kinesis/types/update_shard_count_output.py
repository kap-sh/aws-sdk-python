"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateShardCountOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.positive_integer_object
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_name


class UpdateShardCountOutput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    current_shard_count: NotRequired[
        "aws_sdk_kinesis.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The current number of shards.</p>"""
    target_shard_count: NotRequired[
        "aws_sdk_kinesis.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The updated number of shards.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateShardCountOutput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "current_shard_count" in value:
        out["CurrentShardCount"] = value["current_shard_count"]
    if "target_shard_count" in value:
        out["TargetShardCount"] = value["target_shard_count"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateShardCountOutput:
    out: UpdateShardCountOutput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "CurrentShardCount" in data:
        out["current_shard_count"] = data["CurrentShardCount"]
    if "TargetShardCount" in data:
        out["target_shard_count"] = data["TargetShardCount"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
