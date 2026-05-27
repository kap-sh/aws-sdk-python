"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string
    import aws_sdk_dynamodb.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).</p>"""
    tags: "aws_sdk_dynamodb.types.tag_list.TagList"
    """<p>The tags to be assigned to the Amazon DynamoDB resource.</p>"""
