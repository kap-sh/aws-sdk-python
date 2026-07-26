"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SessionStreamingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs._protocol.eventstream import HeaderValue, Message
from capo_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message


class SessionStreamingException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStreamingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionStreamingException_:
    out: SessionStreamingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SessionStreamingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#SessionStreamingException``."""

    code: str | None = "SessionStreamingException"

    def __init__(self, data: SessionStreamingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionStreamingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SessionStreamingException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: SessionStreamingException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "SessionStreamingException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> SessionStreamingException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SessionStreamingException_ = {}  # type: ignore[typeddict-item]
    return out
