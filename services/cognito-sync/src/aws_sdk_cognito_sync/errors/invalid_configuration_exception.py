"""Generated from Smithy shape ``com.amazonaws.cognitosync#InvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.exception_message


class InvalidConfigurationException_(TypedDict):
    message: "aws_sdk_cognito_sync.types.exception_message.ExceptionMessage"
    """Message returned by InvalidConfigurationException."""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidConfigurationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidConfigurationException_:
    out: InvalidConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidConfigurationException_.message required")
    return out


class InvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InvalidConfigurationException``."""

    code: str | None = "InvalidConfigurationException"

    def __init__(self, data: InvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidConfigurationException":
        return cls(deserialize_json(data))
