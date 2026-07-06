"""Generated from Smithy shape ``com.amazonaws.signin#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_signin.types.o_auth2_error_code


class ConflictException_(TypedDict, closed=True):
    error: "aws_sdk_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating conflict Will be CONFLICT"""
    message: "str"
    """Detailed message explaining the conflict Provides specific information about what caused the conflict"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.o_auth2_error_code

    out["error"] = aws_sdk_signin.types.o_auth2_error_code.serialize_json(
        value["error"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_signin.types.o_auth2_error_code

        out["error"] = aws_sdk_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("ConflictException_.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
