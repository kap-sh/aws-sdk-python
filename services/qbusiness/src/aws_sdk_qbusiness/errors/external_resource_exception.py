"""Generated from Smithy shape ``com.amazonaws.qbusiness#ExternalResourceException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_message


class ExternalResourceException_(TypedDict, closed=True):
    message: "aws_sdk_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: ExternalResourceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExternalResourceException_:
    out: ExternalResourceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ExternalResourceException_.message required")
    return out


class ExternalResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#ExternalResourceException``."""

    code: str | None = "ExternalResourceException"

    def __init__(self, data: ExternalResourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExternalResourceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ExternalResourceException":
        return cls(deserialize_json(data))
