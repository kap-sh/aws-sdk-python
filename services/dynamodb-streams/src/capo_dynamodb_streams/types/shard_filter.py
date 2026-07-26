"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ShardFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.shard_filter_type
    import capo_dynamodb_streams.types.shard_id


class ShardFilter(TypedDict, closed=True):
    type: NotRequired["capo_dynamodb_streams.types.shard_filter_type.ShardFilterType"]
    """<p>Contains the type of filter to be applied on the <code>DescribeStream</code> API. Currently, the only value this parameter accepts is <code>CHILD_SHARDS</code>.</p>"""
    shard_id: NotRequired["capo_dynamodb_streams.types.shard_id.ShardId"]
    """<p>Contains the <code>shardId</code> of the parent shard for which you are requesting child shards.</p> <p> <i>Sample request:</i> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardFilter) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_dynamodb_streams.types.shard_filter_type

        out["Type"] = (
            capo_dynamodb_streams.types.shard_filter_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "shard_id" in value:
        out["ShardId"] = value["shard_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ShardFilter:
    out: ShardFilter = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_dynamodb_streams.types.shard_filter_type

        out["type"] = (
            capo_dynamodb_streams.types.shard_filter_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if "ShardId" in data:
        out["shard_id"] = data["ShardId"]
    return out
