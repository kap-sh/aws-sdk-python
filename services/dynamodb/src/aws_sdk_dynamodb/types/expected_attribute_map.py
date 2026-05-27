"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpectedAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name
    import aws_sdk_dynamodb.types.expected_attribute_value

ExpectedAttributeMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb.types.expected_attribute_value.ExpectedAttributeValue",
]
