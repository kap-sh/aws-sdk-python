"""Generated from Smithy shape ``com.amazonaws.kinesis#ShardIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.shard_id

ShardIdList: TypeAlias = list["aws_sdk_kinesis.types.shard_id.ShardId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ShardIdList:
    return list(data)
