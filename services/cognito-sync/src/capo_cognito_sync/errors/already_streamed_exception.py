"""Generated from Smithy shape ``com.amazonaws.cognitosync#AlreadyStreamedException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class AlreadyStreamedException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """The message associated with the AlreadyStreamedException exception."""


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyStreamedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyStreamedException_:
    out: AlreadyStreamedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AlreadyStreamedException_.message required")
    return out


class AlreadyStreamedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#AlreadyStreamedException``."""

    code: str | None = "AlreadyStreamedException"

    def __init__(self, data: AlreadyStreamedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyStreamedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AlreadyStreamedException":
        return cls(deserialize_json(data))
