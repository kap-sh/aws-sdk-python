"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ShardIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.shard_id

ShardIdList: TypeAlias = list["aws_sdk_keyspacesstreams.types.shard_id.ShardId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ShardIdList:
    return list(data)
