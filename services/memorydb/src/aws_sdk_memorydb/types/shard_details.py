"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.shard_detail

ShardDetails: TypeAlias = list["aws_sdk_memorydb.types.shard_detail.ShardDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardDetails) -> list:
    import aws_sdk_memorydb.types.shard_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.shard_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ShardDetails:
    import aws_sdk_memorydb.types.shard_detail

    out: ShardDetails = []
    for item in data:
        out.append(aws_sdk_memorydb.types.shard_detail.deserialize_aws_json_1_1(item))
    return out
