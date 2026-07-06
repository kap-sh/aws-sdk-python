"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.non_blank_string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ServiceQuotaExceededException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "serviceQuotaExceededException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ServiceQuotaExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    return out
