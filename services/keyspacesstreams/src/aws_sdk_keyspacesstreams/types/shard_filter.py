"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ShardFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.shard_filter_type
    import aws_sdk_keyspacesstreams.types.shard_id


class ShardFilter(TypedDict):
    type: NotRequired[
        "aws_sdk_keyspacesstreams.types.shard_filter_type.ShardFilterType"
    ]
    """<p>The type of shard filter to use, which determines how the shardId parameter is interpreted.</p>"""
    shard_id: NotRequired["aws_sdk_keyspacesstreams.types.shard_id.ShardId"]
    """<p>The identifier of a specific shard used to filter results based on the specified filter type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardFilter) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_keyspacesstreams.types.shard_filter_type

        out["type"] = (
            aws_sdk_keyspacesstreams.types.shard_filter_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "shard_id" in value:
        out["shardId"] = value["shard_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ShardFilter:
    out: ShardFilter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_keyspacesstreams.types.shard_filter_type

        out["type"] = (
            aws_sdk_keyspacesstreams.types.shard_filter_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if "shardId" in data:
        out["shard_id"] = data["shardId"]
    return out
