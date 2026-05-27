"""Generated from Smithy shape ``com.amazonaws.dynamodb#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string
    import aws_sdk_dynamodb.types.tag_key_list


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "aws_sdk_dynamodb.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.</p>"""
