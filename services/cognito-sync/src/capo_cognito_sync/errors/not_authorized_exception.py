"""Generated from Smithy shape ``com.amazonaws.cognitosync#NotAuthorizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class NotAuthorizedException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """The message returned by a NotAuthorizedException."""


# --- restJson1 ser/de ---
def serialize_json(value: NotAuthorizedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotAuthorizedException_:
    out: NotAuthorizedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotAuthorizedException_.message required")
    return out


class NotAuthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#NotAuthorizedException``."""

    code: str | None = "NotAuthorizedException"

    def __init__(self, data: NotAuthorizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAuthorizedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotAuthorizedException":
        return cls(deserialize_json(data))
