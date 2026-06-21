"""Generated from Smithy shape ``com.amazonaws.kinesis#ResourceInUseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis._protocol.eventstream import HeaderValue, Message
from aws_sdk_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.error_message


class ResourceInUseException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(self, data: ResourceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: ResourceInUseException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ResourceInUseException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> ResourceInUseException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    return out
