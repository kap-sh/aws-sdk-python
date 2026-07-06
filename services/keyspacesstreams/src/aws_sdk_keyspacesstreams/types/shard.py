"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.sequence_number_range
    import aws_sdk_keyspacesstreams.types.shard_id
    import aws_sdk_keyspacesstreams.types.shard_id_list


class Shard(TypedDict, closed=True):
    shard_id: NotRequired["aws_sdk_keyspacesstreams.types.shard_id.ShardId"]
    """<p>A unique identifier for this shard within the stream.</p>"""
    sequence_number_range: NotRequired[
        "aws_sdk_keyspacesstreams.types.sequence_number_range.SequenceNumberRange"
    ]
    """<p>The range of sequence numbers contained within this shard.</p>"""
    parent_shard_ids: NotRequired[
        "aws_sdk_keyspacesstreams.types.shard_id_list.ShardIdList"
    ]
    """<p>The identifiers of parent shards that this shard evolved from, if this shard was created through resharding.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Shard) -> dict:
    out: dict = {}
    if "shard_id" in value:
        out["shardId"] = value["shard_id"]
    if "sequence_number_range" in value:
        import aws_sdk_keyspacesstreams.types.sequence_number_range

        out["sequenceNumberRange"] = (
            aws_sdk_keyspacesstreams.types.sequence_number_range.serialize_aws_json_1_0(
                value["sequence_number_range"]
            )
        )
    if "parent_shard_ids" in value:
        import aws_sdk_keyspacesstreams.types.shard_id_list

        out["parentShardIds"] = (
            aws_sdk_keyspacesstreams.types.shard_id_list.serialize_aws_json_1_0(
                value["parent_shard_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if "shardId" in data:
        out["shard_id"] = data["shardId"]
    if "sequenceNumberRange" in data:
        import aws_sdk_keyspacesstreams.types.sequence_number_range

        out["sequence_number_range"] = (
            aws_sdk_keyspacesstreams.types.sequence_number_range.deserialize_aws_json_1_0(
                data["sequenceNumberRange"]
            )
        )
    if "parentShardIds" in data:
        import aws_sdk_keyspacesstreams.types.shard_id_list

        out["parent_shard_ids"] = (
            aws_sdk_keyspacesstreams.types.shard_id_list.deserialize_aws_json_1_0(
                data["parentShardIds"]
            )
        )
    return out
