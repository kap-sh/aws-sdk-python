"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.shard

ShardList: TypeAlias = list["aws_sdk_memorydb.types.shard.Shard"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardList) -> list:
    import aws_sdk_memorydb.types.shard

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.shard.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ShardList:
    import aws_sdk_memorydb.types.shard

    out: ShardList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.shard.deserialize_aws_json_1_1(item))
    return out
