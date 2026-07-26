"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.non_blank_string


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#AccessDeniedException``."""

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
    headers: dict[str, HeaderValue] = {":event-type": "accessDeniedException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AccessDeniedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    return out
