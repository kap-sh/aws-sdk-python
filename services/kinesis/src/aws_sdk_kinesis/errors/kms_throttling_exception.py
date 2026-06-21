"""Generated from Smithy shape ``com.amazonaws.kinesis#KMSThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis._protocol.eventstream import HeaderValue, Message
from aws_sdk_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.error_message


class KMSThrottlingException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSThrottlingException_:
    out: KMSThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#KMSThrottlingException``."""

    code: str | None = "KMSThrottlingException"

    def __init__(self, data: KMSThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSThrottlingException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: KMSThrottlingException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "KMSThrottlingException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> KMSThrottlingException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: KMSThrottlingException_ = {}  # type: ignore[typeddict-item]
    return out
