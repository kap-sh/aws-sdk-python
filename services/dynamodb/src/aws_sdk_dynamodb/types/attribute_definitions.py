"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_definition

AttributeDefinitions: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_definition.AttributeDefinition"
]
