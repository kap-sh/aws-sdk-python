"""Generated from Smithy shape ``com.amazonaws.detective#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_detective.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_detective.types.error_code
    import aws_sdk_detective.types.error_code_reason
    import aws_sdk_detective.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_detective.types.error_message.ErrorMessage"]
    error_code: NotRequired["aws_sdk_detective.types.error_code.ErrorCode"]
    """<p>The SDK default error code associated with the access denied exception.</p>"""
    error_code_reason: NotRequired[
        "aws_sdk_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p>The SDK default explanation of why access was denied.</p>"""
    sub_error_code: NotRequired["aws_sdk_detective.types.error_code.ErrorCode"]
    """<p>The error code associated with the access denied exception.</p>"""
    sub_error_code_reason: NotRequired[
        "aws_sdk_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p> An explanation of why access was denied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
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
    if "sub_error_code" in value:
        import aws_sdk_detective.types.error_code

        out["SubErrorCode"] = aws_sdk_detective.types.error_code.serialize_json(
            value["sub_error_code"]
        )
    if "sub_error_code_reason" in value:
        out["SubErrorCodeReason"] = value["sub_error_code_reason"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        import aws_sdk_detective.types.error_code

        out["error_code"] = aws_sdk_detective.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if "ErrorCodeReason" in data:
        out["error_code_reason"] = data["ErrorCodeReason"]
    if "SubErrorCode" in data:
        import aws_sdk_detective.types.error_code

        out["sub_error_code"] = aws_sdk_detective.types.error_code.deserialize_json(
            data["SubErrorCode"]
        )
    if "SubErrorCodeReason" in data:
        out["sub_error_code_reason"] = data["SubErrorCodeReason"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
