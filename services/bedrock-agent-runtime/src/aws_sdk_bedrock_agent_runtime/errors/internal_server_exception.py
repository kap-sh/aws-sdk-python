"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.non_blank_string


class InternalServerException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    reason: NotRequired["str"]
    """<p>The reason for the exception. If the reason is <code>BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE</code>, the model invocation service is unavailable. Retry your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#InternalServerException``."""

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
    headers: dict[str, HeaderValue] = {":event-type": "internalServerException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InternalServerException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    return out
