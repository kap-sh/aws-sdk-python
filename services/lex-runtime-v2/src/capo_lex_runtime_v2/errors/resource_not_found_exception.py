"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ResourceNotFoundException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ResourceNotFoundException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ResourceNotFoundException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    return out
