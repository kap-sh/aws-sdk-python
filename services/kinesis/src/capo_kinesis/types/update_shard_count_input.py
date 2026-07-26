"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateShardCountInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.positive_integer_object
    import capo_kinesis.types.scaling_type
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class UpdateShardCountInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    target_shard_count: (
        "capo_kinesis.types.positive_integer_object.PositiveIntegerObject"
    )
    """<p>The new number of shards. This value has the following default limits. By default, you cannot do the following: </p> <ul> <li> <p>Set this value to more than double your current shard count for a stream.</p> </li> <li> <p>Set this value below half your current shard count for a stream.</p> </li> <li> <p>Set this value to more than 10000 shards in a stream (the default limit for shard count per stream is 10000 per account per region), unless you request a limit increase.</p> </li> <li> <p>Scale a stream with more than 10000 shards down unless you set this value to less than 10000 shards.</p> </li> </ul>"""
    scaling_type: "capo_kinesis.types.scaling_type.ScalingType"
    """<p>The scaling type. Uniform scaling creates shards of equal size.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateShardCountInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["TargetShardCount"] = value["target_shard_count"]
    import capo_kinesis.types.scaling_type

    out["ScalingType"] = capo_kinesis.types.scaling_type.serialize_aws_json_1_1(
        value["scaling_type"]
    )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateShardCountInput:
    out: UpdateShardCountInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "TargetShardCount" in data:
        out["target_shard_count"] = data["TargetShardCount"]
    else:
        raise DeserializationError("UpdateShardCountInput.target_shard_count required")
    if "ScalingType" in data:
        import capo_kinesis.types.scaling_type

        out["scaling_type"] = capo_kinesis.types.scaling_type.deserialize_aws_json_1_1(
            data["ScalingType"]
        )
    else:
        raise DeserializationError("UpdateShardCountInput.scaling_type required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
