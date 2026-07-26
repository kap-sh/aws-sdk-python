"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message
from capo_transcribe_streaming.errors import ServiceError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.string


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_transcribe_streaming.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transcribestreaming#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))


def serialize_event_json(value: BadRequestException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "BadRequestException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BadRequestException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    return out
