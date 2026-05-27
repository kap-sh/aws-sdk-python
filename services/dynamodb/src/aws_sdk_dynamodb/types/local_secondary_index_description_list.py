"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.local_secondary_index_description

LocalSecondaryIndexDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.local_secondary_index_description.LocalSecondaryIndexDescription"
]
