"""Generated from Smithy shape ``com.amazonaws.dynamodb#SecondaryIndexesCapacityMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.capacity

SecondaryIndexesCapacityMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.index_name.IndexName",
    "aws_sdk_dynamodb.types.capacity.Capacity",
]
