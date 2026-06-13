"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ShardDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.shard

ShardDescriptionList: TypeAlias = list["aws_sdk_keyspacesstreams.types.shard.Shard"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardDescriptionList) -> list:
    import aws_sdk_keyspacesstreams.types.shard

    out: list = []
    for item in value:
        out.append(aws_sdk_keyspacesstreams.types.shard.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ShardDescriptionList:
    import aws_sdk_keyspacesstreams.types.shard

    out: ShardDescriptionList = []
    for item in data:
        out.append(aws_sdk_keyspacesstreams.types.shard.deserialize_aws_json_1_0(item))
    return out
