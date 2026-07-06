"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ConcurrentModificationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codestar_notifications.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.message


class ConcurrentModificationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codestar_notifications.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codestarnotifications#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(self, data: ConcurrentModificationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentModificationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConcurrentModificationException":
        return cls(deserialize_json(data))
