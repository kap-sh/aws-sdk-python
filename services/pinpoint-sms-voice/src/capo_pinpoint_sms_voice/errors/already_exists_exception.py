"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#AlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.string


class AlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint_sms_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoice#AlreadyExistsException``."""

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
