"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InternalStreamFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.message


class InternalStreamFailure_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sagemaker_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalStreamFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalStreamFailure_:
    out: InternalStreamFailure_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalStreamFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#InternalStreamFailure``."""

    code: str | None = "InternalStreamFailure"

    def __init__(self, data: InternalStreamFailure_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalStreamFailure",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalStreamFailure":
        return cls(deserialize_json(data))


def serialize_event_json(value: InternalStreamFailure_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "InternalStreamFailure"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InternalStreamFailure_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalStreamFailure_ = {}  # type: ignore[typeddict-item]
    return out
