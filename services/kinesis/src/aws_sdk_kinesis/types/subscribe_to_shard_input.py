"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.consumer_arn
    import aws_sdk_kinesis.types.shard_id
    import aws_sdk_kinesis.types.starting_position
    import aws_sdk_kinesis.types.stream_id


class SubscribeToShardInput(TypedDict, closed=True):
    consumer_arn: "aws_sdk_kinesis.types.consumer_arn.ConsumerARN"
    """<p>For this parameter, use the value you obtained when you called <a>RegisterStreamConsumer</a>.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    shard_id: "aws_sdk_kinesis.types.shard_id.ShardId"
    """<p>The ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use <a>ListShards</a>.</p>"""
    starting_position: "aws_sdk_kinesis.types.starting_position.StartingPosition"
    """<p>The starting position in the data stream from which to start streaming.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToShardInput) -> dict:
    out: dict = {}
    out["ConsumerARN"] = value["consumer_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["ShardId"] = value["shard_id"]
    import aws_sdk_kinesis.types.starting_position

    out["StartingPosition"] = (
        aws_sdk_kinesis.types.starting_position.serialize_aws_json_1_1(
            value["starting_position"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribeToShardInput:
    out: SubscribeToShardInput = {}  # type: ignore[typeddict-item]
    if "ConsumerARN" in data:
        out["consumer_arn"] = data["ConsumerARN"]
    else:
        raise DeserializationError("SubscribeToShardInput.consumer_arn required")
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    if "ShardId" in data:
        out["shard_id"] = data["ShardId"]
    else:
        raise DeserializationError("SubscribeToShardInput.shard_id required")
    if "StartingPosition" in data:
        import aws_sdk_kinesis.types.starting_position

        out["starting_position"] = (
            aws_sdk_kinesis.types.starting_position.deserialize_aws_json_1_1(
                data["StartingPosition"]
            )
        )
    else:
        raise DeserializationError("SubscribeToShardInput.starting_position required")
    return out
