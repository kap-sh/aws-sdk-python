"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_description

ReplicaDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_description.ReplicaDescription"
]
