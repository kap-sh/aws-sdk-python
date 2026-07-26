"""Generated from Smithy shape ``com.amazonaws.polly#ServiceFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_polly._protocol.eventstream import HeaderValue, Message
from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message


class ServiceFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceFailureException_:
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ServiceFailureException``."""

    code: str | None = "ServiceFailureException"

    def __init__(self, data: ServiceFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceFailureException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ServiceFailureException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ServiceFailureException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ServiceFailureException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    return out
