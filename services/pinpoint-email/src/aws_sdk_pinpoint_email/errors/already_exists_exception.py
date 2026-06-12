"""Generated from Smithy shape ``com.amazonaws.pinpointemail#AlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_email.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.error_message


class AlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_pinpoint_email.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointemail#AlreadyExistsException``."""

    code: str | None = "AlreadyExistsException"

    def __init__(self, data: AlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AlreadyExistsException":
        return cls(deserialize_json(data))
