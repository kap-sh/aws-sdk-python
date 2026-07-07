"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#BadGatewayException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from aws_sdk_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.string


class BadGatewayException_(TypedDict, closed=True):
    message: "aws_sdk_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: BadGatewayException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadGatewayException_:
    out: BadGatewayException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BadGatewayException_.message required")
    return out


class BadGatewayException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#BadGatewayException``."""

    code: str | None = "BadGatewayException"

    def __init__(self, data: BadGatewayException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="BadGatewayException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadGatewayException":
        return cls(deserialize_json(data))


def serialize_event_json(value: BadGatewayException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "BadGatewayException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BadGatewayException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BadGatewayException_ = {}  # type: ignore[typeddict-item]
    return out
