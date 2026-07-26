"""Generated from Smithy shape ``com.amazonaws.kinesis#InternalFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis._protocol.eventstream import HeaderValue, Message
from capo_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis.types.error_message


class InternalFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(self, data: InternalFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalFailureException":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: InternalFailureException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "InternalFailureException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> InternalFailureException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    return out
