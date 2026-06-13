"""Generated from Smithy shape ``com.amazonaws.emr#InvalidRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_emr.types.error_code
    import aws_sdk_emr.types.error_message


class InvalidRequestException_(TypedDict):
    error_code: NotRequired["aws_sdk_emr.types.error_code.ErrorCode"]
    """<p>The error code associated with the exception.</p>"""
    message: NotRequired["aws_sdk_emr.types.error_message.ErrorMessage"]
    """<p>The message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.emr#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data))
