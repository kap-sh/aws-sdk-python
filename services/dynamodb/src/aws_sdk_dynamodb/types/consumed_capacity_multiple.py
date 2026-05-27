"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConsumedCapacityMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity

ConsumedCapacityMultiple: TypeAlias = list[
    "aws_sdk_dynamodb.types.consumed_capacity.ConsumedCapacity"
]
