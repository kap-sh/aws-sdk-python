"""Generated from Smithy shape ``com.amazonaws.kinesis#KMSInvalidStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis._protocol.eventstream import HeaderValue, Message
from aws_sdk_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.error_message


class KMSInvalidStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSInvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSInvalidStateException_:
    out: KMSInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#KMSInvalidStateException``."""

    code: str | None = "KMSInvalidStateException"

    def __init__(self, data: KMSInvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSInvalidStateException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: KMSInvalidStateException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "KMSInvalidStateException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> KMSInvalidStateException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: KMSInvalidStateException_ = {}  # type: ignore[typeddict-item]
    return out
