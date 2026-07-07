"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_blank_string


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ThrottlingException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "throttlingException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ThrottlingException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    return out
