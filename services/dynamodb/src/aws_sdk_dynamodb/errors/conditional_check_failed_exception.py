"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.error_message


class ConditionalCheckFailedException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>The conditional request failed.</p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Item which caused the <code>ConditionalCheckFailedException</code>.</p>"""


class ConditionalCheckFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

    code: str | None = "ConditionalCheckFailedException"

    def __init__(self, data: ConditionalCheckFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionalCheckFailedException",
        )
        self.data = data
