"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.local_secondary_index_info

LocalSecondaryIndexes: TypeAlias = list[
    "aws_sdk_dynamodb.types.local_secondary_index_info.LocalSecondaryIndexInfo"
]
