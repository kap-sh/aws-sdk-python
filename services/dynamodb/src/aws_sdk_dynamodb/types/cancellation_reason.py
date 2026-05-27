"""Generated from Smithy shape ``com.amazonaws.dynamodb#CancellationReason``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.code
    import aws_sdk_dynamodb.types.error_message


class CancellationReason(TypedDict):
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Item in the request which caused the transaction to get cancelled.</p>"""
    code: NotRequired["aws_sdk_dynamodb.types.code.Code"]
    """<p>Status code for the result of the cancelled transaction.</p>"""
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>Cancellation reason message description.</p>"""
