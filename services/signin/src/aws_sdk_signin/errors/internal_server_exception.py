"""Generated from Smithy shape ``com.amazonaws.signin#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_signin.types.o_auth2_error_code


class InternalServerException_(TypedDict, closed=True):
    error: "aws_sdk_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating server error Will be SERVER_ERROR for internal server errors"""
    message: "str"
    """Detailed message explaining the server error May include error details for debugging purposes"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.o_auth2_error_code

    out["error"] = aws_sdk_signin.types.o_auth2_error_code.serialize_json(
        value["error"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_signin.types.o_auth2_error_code

        out["error"] = aws_sdk_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("InternalServerException_.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
