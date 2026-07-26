"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ConcurrentModificationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.error_message


class ConcurrentModificationException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint_email.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointemail#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(self, data: ConcurrentModificationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentModificationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConcurrentModificationException":
        return cls(deserialize_json(data))
