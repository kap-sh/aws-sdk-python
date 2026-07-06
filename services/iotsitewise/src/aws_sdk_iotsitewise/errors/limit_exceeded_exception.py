"""Generated from Smithy shape ``com.amazonaws.iotsitewise#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise._protocol.eventstream import HeaderValue, Message
from aws_sdk_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.error_message


class LimitExceededException_(TypedDict, closed=True):
    message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LimitExceededException_.message required")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#LimitExceededException``."""

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
    headers: dict[str, HeaderValue] = {":event-type": "limitExceededException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> LimitExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    return out
