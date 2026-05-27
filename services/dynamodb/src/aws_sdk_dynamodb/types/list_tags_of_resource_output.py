"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTagsOfResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.next_token_string
    import aws_sdk_dynamodb.types.tag_list


class ListTagsOfResourceOutput(TypedDict):
    tags: NotRequired["aws_sdk_dynamodb.types.tag_list.TagList"]
    """<p>The tags currently associated with the Amazon DynamoDB resource.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.next_token_string.NextTokenString"]
    """<p>If this value is returned, there are additional results to be displayed. To retrieve them, call ListTagsOfResource again, with NextToken set to this value.</p>"""
