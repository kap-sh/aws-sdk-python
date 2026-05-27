"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTagsOfResourceInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.next_token_string
    import aws_sdk_dynamodb.types.resource_arn_string


class ListTagsOfResourceInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.next_token_string.NextTokenString"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to ListTagOfResource. When provided in this manner, this API fetches the next page of results.</p>"""
