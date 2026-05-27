"""Generated from Smithy shape ``com.amazonaws.dynamodb#InvalidEndpointException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.string


class InvalidEndpointException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.string.String"]


class InvalidEndpointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InvalidEndpointException``."""

    code: str | None = "InvalidEndpointException"

    def __init__(self, data: InvalidEndpointException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndpointException",
        )
        self.data = data
