"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#InvalidDeviceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.error_message


class InvalidDeviceException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kinesis_video.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidDeviceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidDeviceException_:
    out: InvalidDeviceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDeviceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideo#InvalidDeviceException``."""

    code: str | None = "InvalidDeviceException"

    def __init__(self, data: InvalidDeviceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDeviceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidDeviceException":
        return cls(deserialize_json(data))
