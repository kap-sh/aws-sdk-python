"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from aws_sdk_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.string


class AccessDeniedException_(TypedDict, closed=True):
    message: "aws_sdk_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))


def serialize_event_json(value: AccessDeniedException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "AccessDeniedException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AccessDeniedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    return out
