"""Generated from Smithy shape ``com.amazonaws.sqs#ReceiptHandleIsInvalid``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class ReceiptHandleIsInvalid_(TypedDict):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiptHandleIsInvalid_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReceiptHandleIsInvalid_:
    out: ReceiptHandleIsInvalid_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReceiptHandleIsInvalid(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#ReceiptHandleIsInvalid``."""

    code: str | None = "ReceiptHandleIsInvalid"

    def __init__(self, data: ReceiptHandleIsInvalid_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReceiptHandleIsInvalid",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ReceiptHandleIsInvalid":
        return cls(deserialize_aws_json_1_0(data))
