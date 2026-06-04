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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactionCanceledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "cancellation_reasons" in value:
        import aws_sdk_dynamodb.types.cancellation_reason_list

        out["CancellationReasons"] = (
            aws_sdk_dynamodb.types.cancellation_reason_list.serialize_aws_json_1_0(
                value["cancellation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactionCanceledException_:
    out: TransactionCanceledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CancellationReasons" in data:
        import aws_sdk_dynamodb.types.cancellation_reason_list

        out["cancellation_reasons"] = (
            aws_sdk_dynamodb.types.cancellation_reason_list.deserialize_aws_json_1_0(
                data["CancellationReasons"]
            )
        )
    return out


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

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TransactionCanceledException":
        return cls(deserialize_aws_json_1_0(data))
