"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from aws_sdk_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.string


class InternalServerException_(TypedDict):
    message: "aws_sdk_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))


def serialize_event_json(value: InternalServerException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "InternalServerException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InternalServerException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    return out
