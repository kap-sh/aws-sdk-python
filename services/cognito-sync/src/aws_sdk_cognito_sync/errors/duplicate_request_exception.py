"""Generated from Smithy shape ``com.amazonaws.cognitosync#DuplicateRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.exception_message


class DuplicateRequestException_(TypedDict, closed=True):
    message: "aws_sdk_cognito_sync.types.exception_message.ExceptionMessage"
    """The message associated with the DuplicateRequestException exception."""


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateRequestException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DuplicateRequestException_:
    out: DuplicateRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DuplicateRequestException_.message required")
    return out


class DuplicateRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#DuplicateRequestException``."""

    code: str | None = "DuplicateRequestException"

    def __init__(self, data: DuplicateRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DuplicateRequestException":
        return cls(deserialize_json(data))
