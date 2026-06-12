"""Generated from Smithy shape ``com.amazonaws.signin#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_signin.types.o_auth2_error_code


class AccessDeniedException_(TypedDict):
    error: "aws_sdk_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating the specific type of access denial Can be TOKEN_EXPIRED, AUTHCODE_EXPIRED, USER_CREDENTIALS_CHANGED, or INSUFFICIENT_PERMISSIONS"""
    message: "str"
    """Detailed message explaining the access denial Provides specific information about why access was denied"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.o_auth2_error_code

    out["error"] = aws_sdk_signin.types.o_auth2_error_code.serialize_json(
        value["error"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_signin.types.o_auth2_error_code

        out["error"] = aws_sdk_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("AccessDeniedException_.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#AccessDeniedException``."""

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
