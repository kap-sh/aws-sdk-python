"""Generated from Smithy shape ``com.amazonaws.s3files#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.error_code


class ValidationException_(TypedDict):
    error_code: "aws_sdk_s3files.types.error_code.ErrorCode"
    """<p>The error code associated with the exception.</p>"""
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ValidationException_.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3files#ValidationException``."""

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
