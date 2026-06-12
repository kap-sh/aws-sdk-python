"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidAccessPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_code
    import aws_sdk_fsx.types.error_message


class InvalidAccessPoint_(TypedDict):
    error_code: NotRequired["aws_sdk_fsx.types.error_code.ErrorCode"]
    """<p>An error code indicating that the access point specified doesn't exist.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAccessPoint_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAccessPoint_:
    out: InvalidAccessPoint_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidAccessPoint(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidAccessPoint``."""

    code: str | None = "InvalidAccessPoint"

    def __init__(self, data: InvalidAccessPoint_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAccessPoint",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidAccessPoint":
        return cls(deserialize_aws_json_1_1(data))
