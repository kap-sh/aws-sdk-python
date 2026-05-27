"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactionCanceledException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.cancellation_reason_list
    import aws_sdk_dynamodb.types.error_message


class TransactionCanceledException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    cancellation_reasons: NotRequired[
        "aws_sdk_dynamodb.types.cancellation_reason_list.CancellationReasonList"
    ]
    """<p>A list of cancellation reasons.</p>"""


class TransactionCanceledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TransactionCanceledException``."""

    code: str | None = "TransactionCanceledException"

    def __init__(self, data: TransactionCanceledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCanceledException",
        )
        self.data = data
