"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactionInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class TransactionInProgressException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactionInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactionInProgressException_:
    out: TransactionInProgressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TransactionInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TransactionInProgressException``."""

    code: str | None = "TransactionInProgressException"

    def __init__(self, data: TransactionInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TransactionInProgressException":
        return cls(deserialize_aws_json_1_0(data))
