"""Generated from Smithy shape ``com.amazonaws.connecthealth#ValidationException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth._protocol.eventstream import HeaderValue, Message
from aws_sdk_connecthealth.errors import ServiceError


class ValidationException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connecthealth#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ValidationException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "validationException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ValidationException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    return out
