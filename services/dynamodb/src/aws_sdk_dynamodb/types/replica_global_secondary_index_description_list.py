"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_description

ReplicaGlobalSecondaryIndexDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_description.ReplicaGlobalSecondaryIndexDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndexDescriptionList) -> list:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaGlobalSecondaryIndexDescriptionList:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_description

    out: ReplicaGlobalSecondaryIndexDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
