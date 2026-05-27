"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.local_secondary_index

LocalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_dynamodb.types.local_secondary_index.LocalSecondaryIndex"
]
