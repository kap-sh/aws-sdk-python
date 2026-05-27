"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.availability_error_message
    import aws_sdk_dynamodb.types.throttling_reason_list


class ThrottlingException_(TypedDict):
    message: NotRequired[
        "aws_sdk_dynamodb.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "aws_sdk_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html\">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data
