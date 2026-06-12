"""Generated from Smithy shape ``com.amazonaws.detective#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_detective.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_detective.types.error_code
    import aws_sdk_detective.types.error_code_reason
    import aws_sdk_detective.types.error_message


class ValidationException_(TypedDict):
    message: NotRequired["aws_sdk_detective.types.error_message.ErrorMessage"]
    error_code: NotRequired["aws_sdk_detective.types.error_code.ErrorCode"]
    """<p>The error code associated with the validation failure.</p>"""
    error_code_reason: NotRequired[
        "aws_sdk_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p> An explanation of why validation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        import aws_sdk_detective.types.error_code

        out["ErrorCode"] = aws_sdk_detective.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_code_reason" in value:
        out["ErrorCodeReason"] = value["error_code_reason"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        import aws_sdk_detective.types.error_code

        out["error_code"] = aws_sdk_detective.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if "ErrorCodeReason" in data:
        out["error_code_reason"] = data["ErrorCodeReason"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))
