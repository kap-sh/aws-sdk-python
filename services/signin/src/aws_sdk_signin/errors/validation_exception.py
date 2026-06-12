"""Generated from Smithy shape ``com.amazonaws.signin#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_signin.types.o_auth2_error_code


class ValidationException_(TypedDict):
    error: "aws_sdk_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating validation failure Will be INVALID_REQUEST for validation errors"""
    message: "str"
    """Detailed message explaining the validation failure Provides specific information about which validation failed"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.o_auth2_error_code

    out["error"] = aws_sdk_signin.types.o_auth2_error_code.serialize_json(
        value["error"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_signin.types.o_auth2_error_code

        out["error"] = aws_sdk_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("ValidationException_.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#ValidationException``."""

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
