"""Generated from Smithy shape ``com.amazonaws.qbusiness#MediaTooLargeException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_message


class MediaTooLargeException_(TypedDict):
    message: "aws_sdk_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: MediaTooLargeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MediaTooLargeException_:
    out: MediaTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("MediaTooLargeException_.message required")
    return out


class MediaTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#MediaTooLargeException``."""

    code: str | None = "MediaTooLargeException"

    def __init__(self, data: MediaTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MediaTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MediaTooLargeException":
        return cls(deserialize_json(data))
