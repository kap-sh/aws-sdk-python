"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#TransactionInProgressException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class TransactionInProgressException_(TypedDict):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransactionInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransactionInProgressException_:
    out: TransactionInProgressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TransactionInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#TransactionInProgressException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "TransactionInProgressException":
        return cls(deserialize_aws_json_1_1(data))
