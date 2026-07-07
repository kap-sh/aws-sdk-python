"""Generated from Smithy shape ``com.amazonaws.polly#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly._protocol.eventstream import HeaderValue, Message
from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.availability_error_message
    import aws_sdk_polly.types.throttling_reason_list


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_polly.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "aws_sdk_polly.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of reasons explaining why the request was throttled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import aws_sdk_polly.types.throttling_reason_list

        out["throttlingReasons"] = (
            aws_sdk_polly.types.throttling_reason_list.serialize_json(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "throttlingReasons" in data:
        import aws_sdk_polly.types.throttling_reason_list

        out["throttling_reasons"] = (
            aws_sdk_polly.types.throttling_reason_list.deserialize_json(
                data["throttlingReasons"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ThrottlingException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ThrottlingException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ThrottlingException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    return out
