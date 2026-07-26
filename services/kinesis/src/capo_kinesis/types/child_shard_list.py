"""Generated from Smithy shape ``com.amazonaws.kinesis#ChildShardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.child_shard

ChildShardList: TypeAlias = list["capo_kinesis.types.child_shard.ChildShard"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildShardList) -> list:
    import capo_kinesis.types.child_shard

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.child_shard.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ChildShardList:
    import capo_kinesis.types.child_shard

    out: ChildShardList = []
    for item in data:
        out.append(capo_kinesis.types.child_shard.deserialize_aws_json_1_1(item))
    return out
