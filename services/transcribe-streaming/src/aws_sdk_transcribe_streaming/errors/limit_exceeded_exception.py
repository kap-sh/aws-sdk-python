"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe_streaming._protocol.eventstream import HeaderValue, Message
from aws_sdk_transcribe_streaming.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.string


class LimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transcribestreaming#LimitExceededException``."""

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


def serialize_event_json(value: LimitExceededException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "LimitExceededException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> LimitExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    return out
