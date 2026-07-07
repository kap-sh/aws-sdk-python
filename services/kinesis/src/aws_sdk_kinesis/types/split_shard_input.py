"""Generated from Smithy shape ``com.amazonaws.kinesis#SplitShardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.hash_key
    import aws_sdk_kinesis.types.shard_id
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class SplitShardInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream for the shard split.</p>"""
    shard_to_split: "aws_sdk_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the shard to split.</p>"""
    new_starting_hash_key: "aws_sdk_kinesis.types.hash_key.HashKey"
    """<p>A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for <code>NewStartingHashKey</code> must be in the range of hash keys being mapped into the shard. The <code>NewStartingHashKey</code> hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitShardInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["ShardToSplit"] = value["shard_to_split"]
    out["NewStartingHashKey"] = value["new_starting_hash_key"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitShardInput:
    out: SplitShardInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "ShardToSplit" in data:
        out["shard_to_split"] = data["ShardToSplit"]
    else:
        raise DeserializationError("SplitShardInput.shard_to_split required")
    if "NewStartingHashKey" in data:
        out["new_starting_hash_key"] = data["NewStartingHashKey"]
    else:
        raise DeserializationError("SplitShardInput.new_starting_hash_key required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
