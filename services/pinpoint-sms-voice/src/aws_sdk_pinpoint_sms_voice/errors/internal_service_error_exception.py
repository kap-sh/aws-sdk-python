"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.string


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoice#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(self, data: InternalServiceErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceErrorException":
        return cls(deserialize_json(data))
