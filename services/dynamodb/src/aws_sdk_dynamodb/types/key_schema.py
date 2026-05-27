"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeySchema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key_schema_element

KeySchema: TypeAlias = list[
    "aws_sdk_dynamodb.types.key_schema_element.KeySchemaElement"
]
