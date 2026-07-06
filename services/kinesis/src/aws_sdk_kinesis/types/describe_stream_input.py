"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.describe_stream_input_limit
    import aws_sdk_kinesis.types.shard_id
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class DescribeStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to describe.</p>"""
    limit: NotRequired[
        "aws_sdk_kinesis.types.describe_stream_input_limit.DescribeStreamInputLimit"
    ]
    """<p>The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>"""
    exclusive_start_shard_id: NotRequired["aws_sdk_kinesis.types.shard_id.ShardId"]
    """<p>The shard ID of the shard to start with.</p> <p>Specify this parameter to indicate that you want to describe the stream starting with the shard whose ID immediately follows <code>ExclusiveStartShardId</code>.</p> <p>If you don't specify this parameter, the default behavior for <code>DescribeStream</code> is to describe the stream starting with the first shard in the stream.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_shard_id" in value:
        out["ExclusiveStartShardId"] = value["exclusive_start_shard_id"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamInput:
    out: DescribeStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "ExclusiveStartShardId" in data:
        out["exclusive_start_shard_id"] = data["ExclusiveStartShardId"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
