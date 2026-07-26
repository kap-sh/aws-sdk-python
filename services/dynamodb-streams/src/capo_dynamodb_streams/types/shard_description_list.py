"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ShardDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.shard

ShardDescriptionList: TypeAlias = list["capo_dynamodb_streams.types.shard.Shard"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardDescriptionList) -> list:
    import capo_dynamodb_streams.types.shard

    out: list = []
    for item in value:
        out.append(capo_dynamodb_streams.types.shard.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ShardDescriptionList:
    import capo_dynamodb_streams.types.shard

    out: ShardDescriptionList = []
    for item in data:
        out.append(capo_dynamodb_streams.types.shard.deserialize_aws_json_1_0(item))
    return out
