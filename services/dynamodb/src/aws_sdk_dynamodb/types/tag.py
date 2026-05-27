"""Generated from Smithy shape ``com.amazonaws.dynamodb#Tag``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.tag_key_string
    import aws_sdk_dynamodb.types.tag_value_string


class Tag(TypedDict):
    key: "aws_sdk_dynamodb.types.tag_key_string.TagKeyString"
    """<p>The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.</p>"""
    value: "aws_sdk_dynamodb.types.tag_value_string.TagValueString"
    """<p>The value of the tag. Tag values are case-sensitive and can be null.</p>"""
