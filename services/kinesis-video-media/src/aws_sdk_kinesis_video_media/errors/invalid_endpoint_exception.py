"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#InvalidEndpointException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_media.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_media.types.error_message


class InvalidEndpointException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis_video_media.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidEndpointException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidEndpointException_:
    out: InvalidEndpointException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidEndpointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideomedia#InvalidEndpointException``."""

    code: str | None = "InvalidEndpointException"

    def __init__(self, data: InvalidEndpointException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndpointException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidEndpointException":
        return cls(deserialize_json(data))
