"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughputExceededException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message
    import aws_sdk_dynamodb.types.throttling_reason_list


class ProvisionedThroughputExceededException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>You exceeded your maximum allowed provisioned throughput.</p>"""
    throttling_reasons: NotRequired[
        "aws_sdk_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html\">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


class ProvisionedThroughputExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughputExceededException``."""

    code: str | None = "ProvisionedThroughputExceededException"

    def __init__(self, data: ProvisionedThroughputExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProvisionedThroughputExceededException",
        )
        self.data = data
