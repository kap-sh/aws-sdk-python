"""Generated from Smithy shape ``com.amazonaws.kinesis#KMSOptInRequired``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis._protocol.eventstream import HeaderValue, Message
from capo_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis.types.error_message


class KMSOptInRequired_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSOptInRequired_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSOptInRequired_:
    out: KMSOptInRequired_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSOptInRequired(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#KMSOptInRequired``."""

    code: str | None = "KMSOptInRequired"

    def __init__(self, data: KMSOptInRequired_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSOptInRequired",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSOptInRequired":
        return cls(deserialize_aws_json_1_1(data))


def serialize_event_aws_json_1_1(value: KMSOptInRequired_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "KMSOptInRequired"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> KMSOptInRequired_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: KMSOptInRequired_ = {}  # type: ignore[typeddict-item]
    return out
