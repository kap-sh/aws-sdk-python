"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SessionTimeoutException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs._protocol.eventstream import HeaderValue, Message
from aws_sdk_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.message


class SessionTimeoutException_(TypedDict):
    message: NotRequired["aws_sdk_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionTimeoutException_:
    out: SessionTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SessionTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#SessionTimeoutException``."""

    code: str | None = "SessionTimeoutException"

    def __init__(self, data: SessionTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionTimeoutException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SessionTimeoutException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: SessionTimeoutException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "SessionTimeoutException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> SessionTimeoutException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SessionTimeoutException_ = {}  # type: ignore[typeddict-item]
    return out
