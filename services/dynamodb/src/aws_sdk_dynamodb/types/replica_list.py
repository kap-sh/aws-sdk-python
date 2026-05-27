"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica

ReplicaList: TypeAlias = list["aws_sdk_dynamodb.types.replica.Replica"]
