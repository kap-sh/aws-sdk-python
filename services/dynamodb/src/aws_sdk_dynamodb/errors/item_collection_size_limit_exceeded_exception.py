"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ItemCollectionSizeLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>The total size of an item collection has exceeded the maximum limit of 10 gigabytes.</p>"""


class ItemCollectionSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

    code: str | None = "ItemCollectionSizeLimitExceededException"

    def __init__(self, data: ItemCollectionSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemCollectionSizeLimitExceededException",
        )
        self.data = data
