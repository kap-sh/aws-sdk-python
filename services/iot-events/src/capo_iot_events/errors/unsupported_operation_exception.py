"""Generated from Smithy shape ``com.amazonaws.iotevents#UnsupportedOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_events.types.error_message


class UnsupportedOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_events.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedOperationException_:
    out: UnsupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotevents#UnsupportedOperationException``."""

    code: str | None = "UnsupportedOperationException"

    def __init__(self, data: UnsupportedOperationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedOperationException":
        return cls(deserialize_json(data))
