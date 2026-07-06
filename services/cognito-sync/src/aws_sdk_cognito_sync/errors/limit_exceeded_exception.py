"""Generated from Smithy shape ``com.amazonaws.cognitosync#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.exception_message


class LimitExceededException_(TypedDict, closed=True):
    message: "aws_sdk_cognito_sync.types.exception_message.ExceptionMessage"
    """Message returned by LimitExceededException."""


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LimitExceededException_.message required")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_json(data))
