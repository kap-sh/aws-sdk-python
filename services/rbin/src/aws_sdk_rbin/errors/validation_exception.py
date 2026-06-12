"""Generated from Smithy shape ``com.amazonaws.rbin#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rbin.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rbin.types.error_message
    import aws_sdk_rbin.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: NotRequired["aws_sdk_rbin.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "aws_sdk_rbin.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_rbin.types.validation_exception_reason

        out["Reason"] = aws_sdk_rbin.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_rbin.types.validation_exception_reason

        out["reason"] = aws_sdk_rbin.types.validation_exception_reason.deserialize_json(
            data["Reason"]
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rbin#ValidationException``."""

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
