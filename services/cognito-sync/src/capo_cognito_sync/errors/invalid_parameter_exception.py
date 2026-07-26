"""Generated from Smithy shape ``com.amazonaws.cognitosync#InvalidParameterException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class InvalidParameterException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """Message returned by InvalidParameterException."""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidParameterException_.message required")
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_json(data))
