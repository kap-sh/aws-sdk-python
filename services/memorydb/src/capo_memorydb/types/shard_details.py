"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.shard_detail

ShardDetails: TypeAlias = list["capo_memorydb.types.shard_detail.ShardDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardDetails) -> list:
    import capo_memorydb.types.shard_detail

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.shard_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ShardDetails:
    import capo_memorydb.types.shard_detail

    out: ShardDetails = []
    for item in data:
        out.append(capo_memorydb.types.shard_detail.deserialize_aws_json_1_1(item))
    return out
