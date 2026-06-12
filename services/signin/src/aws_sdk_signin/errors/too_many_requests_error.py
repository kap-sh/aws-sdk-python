"""Generated from Smithy shape ``com.amazonaws.signin#TooManyRequestsError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_signin.types.o_auth2_error_code


class TooManyRequestsError_(TypedDict):
    error: "aws_sdk_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating the specific type of error Will be INVALID_REQUEST for rate limiting scenarios"""
    message: "str"
    """Detailed message about the rate limiting May include retry-after information or rate limit details"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsError_) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.o_auth2_error_code

    out["error"] = aws_sdk_signin.types.o_auth2_error_code.serialize_json(
        value["error"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsError_:
    out: TooManyRequestsError_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_signin.types.o_auth2_error_code

        out["error"] = aws_sdk_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("TooManyRequestsError_.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TooManyRequestsError_.message required")
    return out


class TooManyRequestsError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#TooManyRequestsError``."""

    code: str | None = "TooManyRequestsError"

    def __init__(self, data: TooManyRequestsError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsError":
        return cls(deserialize_json(data))
