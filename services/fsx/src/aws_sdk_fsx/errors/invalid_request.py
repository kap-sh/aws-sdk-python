"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_code
    import aws_sdk_fsx.types.error_message


class InvalidRequest_(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_fsx.types.error_code.ErrorCode"]
    """<p>An error code indicating that the action or operation requested is invalid.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequest_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequest_:
    out: InvalidRequest_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidRequest``."""

    code: str | None = "InvalidRequest"

    def __init__(self, data: InvalidRequest_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequest",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRequest":
        return cls(deserialize_aws_json_1_1(data))
