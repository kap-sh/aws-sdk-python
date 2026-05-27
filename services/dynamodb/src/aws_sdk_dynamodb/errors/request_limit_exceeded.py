"""Generated from Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message
    import aws_sdk_dynamodb.types.throttling_reason_list


class RequestLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    throttling_reasons: NotRequired[
        "aws_sdk_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html\">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


class RequestLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

    code: str | None = "RequestLimitExceeded"

    def __init__(self, data: RequestLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestLimitExceeded",
        )
        self.data = data
