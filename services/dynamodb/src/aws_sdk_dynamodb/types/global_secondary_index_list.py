"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_index

GlobalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_secondary_index.GlobalSecondaryIndex"
]
