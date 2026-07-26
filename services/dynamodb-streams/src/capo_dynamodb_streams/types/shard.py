"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.sequence_number_range
    import capo_dynamodb_streams.types.shard_id


class Shard(TypedDict, closed=True):
    shard_id: NotRequired["capo_dynamodb_streams.types.shard_id.ShardId"]
    """<p>The system-generated identifier for this shard.</p>"""
    sequence_number_range: NotRequired[
        "capo_dynamodb_streams.types.sequence_number_range.SequenceNumberRange"
    ]
    """<p>The range of possible sequence numbers for the shard.</p>"""
    parent_shard_id: NotRequired["capo_dynamodb_streams.types.shard_id.ShardId"]
    """<p>The shard ID of the current shard's parent.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Shard) -> dict:
    out: dict = {}
    if "shard_id" in value:
        out["ShardId"] = value["shard_id"]
    if "sequence_number_range" in value:
        import capo_dynamodb_streams.types.sequence_number_range

        out["SequenceNumberRange"] = (
            capo_dynamodb_streams.types.sequence_number_range.serialize_aws_json_1_0(
                value["sequence_number_range"]
            )
        )
    if "parent_shard_id" in value:
        out["ParentShardId"] = value["parent_shard_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if "ShardId" in data:
        out["shard_id"] = data["ShardId"]
    if "SequenceNumberRange" in data:
        import capo_dynamodb_streams.types.sequence_number_range

        out["sequence_number_range"] = (
            capo_dynamodb_streams.types.sequence_number_range.deserialize_aws_json_1_0(
                data["SequenceNumberRange"]
            )
        )
    if "ParentShardId" in data:
        out["parent_shard_id"] = data["ParentShardId"]
    return out
