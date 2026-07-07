"""Generated from Smithy shape ``com.amazonaws.sqs#UnsupportedOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class UnsupportedOperation_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedOperation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedOperation_:
    out: UnsupportedOperation_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedOperation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#UnsupportedOperation``."""

    code: str | None = "UnsupportedOperation"

    def __init__(self, data: UnsupportedOperation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedOperation",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "UnsupportedOperation":
        return cls(deserialize_aws_json_1_0(data))
