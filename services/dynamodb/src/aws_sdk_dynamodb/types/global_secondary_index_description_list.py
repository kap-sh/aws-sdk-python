"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_index_description

GlobalSecondaryIndexDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_secondary_index_description.GlobalSecondaryIndexDescription"
]
