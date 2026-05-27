"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_description

ReplicaGlobalSecondaryIndexDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_description.ReplicaGlobalSecondaryIndexDescription"
]
